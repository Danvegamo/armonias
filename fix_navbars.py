import os
import re

base_dir = r"c:\Users\Danvegamo\Downloads\pagina.armonias"

nav_template = """<nav class="navbar">
            <a href="{prefix}index.html">
                <img src="{prefix}img/logo.png" alt="Logo">
            </a>
            <span class="menu-toggle">☰</span>
            <ul>
                <li><a href="{prefix}sections/actividades.html">Actividades</a></li>
                <li><a href="{prefix}sections/preparacion.html">Preparación</a></li>
                <li><a href="{prefix}sections/abtus.html">Sobre nosotros</a></li>
            </ul>
            <a class="contact" href="#">Contactate con nosotros</a>
            <script src="{prefix}armonias.js"></script>
        </nav>"""

def unify_navbars(filepath, is_root):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    prefix = '' if is_root else '../'
    nav_html = nav_template.format(prefix=prefix)

    # Use regex to find and replace everything from <nav class="navbar"> to </nav>
    # Handle optional whitespace or newlines inside
    new_content = re.sub(
        r'<nav\s+class="navbar".*?</nav>',
        nav_html,
        content,
        flags=re.DOTALL
    )

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

# Process root files
for root_file in ['index.html', 'prueba.html']:
    fp = os.path.join(base_dir, root_file)
    if os.path.exists(fp):
        unify_navbars(fp, True)

# Process subdirectories
for subdir in ['sections', 'actividades', 'preparacion']:
    dpath = os.path.join(base_dir, subdir)
    if os.path.exists(dpath):
        for fn in os.listdir(dpath):
            if fn.endswith('.html'):
                unify_navbars(os.path.join(dpath, fn), False)
print('Navbars unified!')
