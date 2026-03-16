import os
import re

base_dir = r"c:\Users\Danvegamo\Downloads\pagina.armonias"

def update_links(filepath, is_root):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    prefix = '' if is_root else '../'

    # Fix root absolute links /something -> prefix + something
    content = re.sub(r'href="/([^#"]+)"', lambda m: 'href="' + prefix + m.group(1) + '"', content)
    content = re.sub(r"href='/([^#']+)'", lambda m: "href='" + prefix + m.group(1) + "'", content)
    
    content = re.sub(r'src="/([^#"]+)"', lambda m: 'src="' + prefix + m.group(1) + '"', content)
    content = re.sub(r"src='/([^#']+)'", lambda m: "src='" + prefix + m.group(1) + "'", content)

    # Some scripts / css might be relative instead of absolute, but need ../ in subfolders
    if not is_root:
        # e.g., src="armonias.js" -> src="../armonias.js"
        # We need to make sure we don't duplicate ../../armonias.js so we'll do:
        content = re.sub(r'(?<!../)src="armonias\.js"', r'src="../armonias.js"', content)
        content = re.sub(r'(?<!../)href="armonias\.css"', r'href="../armonias.css"', content)

    # Fix onclick location.href
    if is_root:
        content = re.sub(r"location\.href='act(\d+)\.html'", r"location.href='actividades/act\1.html'", content)
        content = re.sub(r"location\.href='page(\d+)\.html'", r"location.href='actividades/act\1.html'", content) 
        content = re.sub(r"location\.href='actividades\.html'", r"location.href='sections/actividades.html'", content)
        content = re.sub(r"location\.href='preparacion\.html'", r"location.href='sections/preparacion.html'", content)
    else:
        # e.g., location.href='page2.html' -> location.href='../actividades/act2.html'
        # if we are ALREADY in actividades folder, 'page2.html' would be 'act2.html'
        if "actividades" in filepath:
            content = re.sub(r"location\.href='page(\d+)\.html'", r"location.href='act\1.html'", content)
            content = re.sub(r"location\.href='act(\d+)\.html'", r"location.href='act\1.html'", content)
            content = re.sub(r"location\.href='actividades\.html'", r"location.href='../sections/actividades.html'", content)
            content = re.sub(r"location\.href='preparacion\.html'", r"location.href='../sections/preparacion.html'", content)
        else:
            content = re.sub(r"location\.href='page(\d+)\.html'", r"location.href='../actividades/act\1.html'", content)
            content = re.sub(r"location\.href='act(\d+)\.html'", r"location.href='../actividades/act\1.html'", content)
            content = re.sub(r"location\.href='actividades\.html'", r"location.href='../sections/actividades.html'", content)
            content = re.sub(r"location\.href='preparacion\.html'", r"location.href='../sections/preparacion.html'", content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Process root files
for root_file in ['index.html', 'prueba.html']:
    fp = os.path.join(base_dir, root_file)
    if os.path.exists(fp):
        update_links(fp, True)

# Process subdirectories
for subdir in ['sections', 'actividades', 'preparacion']:
    dpath = os.path.join(base_dir, subdir)
    if os.path.exists(dpath):
        for fn in os.listdir(dpath):
            if fn.endswith('.html'):
                update_links(os.path.join(dpath, fn), False)
print('Done!')
