"""
Translator dari skema JSON ke sistem sympy.physics.mechanics (Kane's Method).
"""

from sympy.physics.mechanics import dynamicsymbols, ReferenceFrame, Point, Particle, KanesMethod
from sympy import symbols
from mechanics_registry import SUPPORTED_ARAH_GERAK, SUPPORTED_GAYA, validate_system_def

def bangun_sistem_kanes(skema: dict):
    """
    Membangun sistem Kane's Method dari skema JSON.
    
    Args:
        skema: dict dengan format mekanika (lihat mechanics_schema.md)
    
    Returns:
        tuple: (KanesMethod, dict) di mana dict berisi:
            - q: generalized coordinate
            - u: generalized speed
            - qd: derivative of q
            - particles: list of Particle
            - titik_map: dict mapping id benda ke Point
            - simbol: dict simbol-simbol yang dipakai
    """
    validate_system_def(skema)
    
    # Buat ReferenceFrame
    N = ReferenceFrame('N')
    
    # Buat titik origin
    O = Point('O')
    O.set_vel(N, 0)
    
    # Buat koordinat umum (1 DOF)
    q = dynamicsymbols('q')
    u = dynamicsymbols('u')
    qd = dynamicsymbols('q', 1)
    
    # Kinematical differential equations
    kd = [qd - u]
    
    # Kumpulkan semua benda dan gaya
    particles = []
    titik_map = {}
    loads = []
    all_symbols = {}
    
    # Proses setiap benda
    for benda in skema["benda"]:
        benda_id = benda["id"]
        massa_simbol = benda["massa_simbol"]
        m = symbols(massa_simbol, positive=True)
        all_symbols[massa_simbol] = m
        
        # Dapatkan arah gerak
        tipe_arah = benda["arah_gerak"]["tipe"]
        param_arah = benda["arah_gerak"].get("parameter", {})
        tanda = benda["arah_gerak"].get("tanda", 1)
        
        # Buat simbol sudut jika diperlukan
        if "sudut" in param_arah:
            theta = symbols('theta', positive=True)
            all_symbols['theta'] = theta
        
        # Dapatkan unit vector arah (sudah dalam sympy)
        arah_unit = SUPPORTED_ARAH_GERAK[tipe_arah](N)
        
        # Terapkan tanda: jika tanda = 1, gerak searah q; jika -1, berlawanan
        arah_gerak = tanda * arah_unit
        
        # Buat titik untuk benda ini
        titik = O.locatenew(benda_id, q * arah_gerak)
        titik.set_vel(N, u * arah_gerak)
        titik_map[benda_id] = titik
        
        # Buat Particle
        P = Particle(benda_id, titik, m)
        particles.append(P)
    
    # Tambahkan simbol standar
    g = symbols('g', positive=True)
    mu = symbols('mu', positive=True)
    all_symbols['g'] = g
    all_symbols['mu'] = mu
    
    # Proses setiap gaya
    for gaya in skema["gaya"]:
        tipe_gaya = gaya["tipe"]
        benda_id = gaya["benda"]
        benda_def = next(b for b in skema["benda"] if b["id"] == benda_id)
        
        # Panggil fungsi dari registry
        load = SUPPORTED_GAYA[tipe_gaya](benda_def, skema, N, titik_map)
        loads.append(load)
    
    # Bangun KanesMethod
    q_ind = [q]
    u_ind = [u]
    KM = KanesMethod(N, q_ind=q_ind, u_ind=u_ind, kd_eqs=kd)
    fr, frstar = KM.kanes_equations(particles, loads=loads)
    
    return KM, {
        'q': q,
        'u': u,
        'qd': qd,
        'particles': particles,
        'titik_map': titik_map,
        'simbol': all_symbols,
        'N': N,
        'O': O,
        'fr': fr,
        'frstar': frstar,
    }
