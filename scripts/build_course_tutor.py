"""Regenerate the inline tutor and content-based version after course text changes."""
from pathlib import Path
import json,html,hashlib
from datetime import datetime
from zoneinfo import ZoneInfo
ROOT=Path(__file__).resolve().parents[1]
ASSETS=ROOT/'assets/teaching/management-science-2026-fall'
OUT=ROOT/'_includes/course-tutor'
URL='https://kitaekim0819.github.io/teaching/management-science-2026-fall/'
def esc(text):
    return html.escape(text).replace('{','&#123;').replace('}','&#125;')
manifest=json.loads((ASSETS/'materials.json').read_text())
instructions=(ASSETS/'TUTOR_WEB_INSTRUCTIONS.md').read_text()
texts=[(ASSETS/f['text_url'].rsplit('/',1)[-1]).read_text() for f in manifest['files']]
revision=hashlib.sha256((instructions+json.dumps(manifest,sort_keys=True)+''.join(texts)).encode()).hexdigest()[:12]
version=datetime.now(ZoneInfo('Asia/Seoul')).date().isoformat()
start_url=URL+'?v='+version+'-'+revision
prompt=(f'Read the tutor instructions at {start_url} and act as kau-ms-tutor for this conversation. '
        'State the Materials version actually visible on the page, and guide me one hint at a time. '
        'For questions about course content, read the matching HTML text page listed below FIRST; '
        'these pages contain extracted document text and do not require opening or downloading a PDF, DOCX, or notebook. '
        'Open only the reference needed for my question, not all references. '
        'If the main page is truncated or its collapsed reference sections are omitted, use the corresponding HTML text URL below. '
        'A blocked original PDF does not establish that its HTML text is unavailable. '
        'Only report an access failure for the source you actually tried; do not infer a security restriction without evidence. '
        'If the relevant HTML text is also inaccessible, say so clearly and ask me to paste that section. '
        'Respect tool access restrictions and do not invent content.\n\nHTML course references (use these text pages before original-document links):\n')
for f in manifest['files']:
    title=(f['group']+' — ' if f['group'] else '')+f['title'].replace('Assginment','Assignment')
    prompt+=f"- {title}: {f['web_text_url']}?v={revision}\n"

OUT.mkdir(parents=True,exist_ok=True)
(OUT/'start.html').write_text(f'''<p><strong>Materials version: <code>{version}</code></strong> · {len(texts)} references</p>
<label for="tutor-start-prompt">Copy this prompt into a new AI chat:</label>
<textarea id="tutor-start-prompt" readonly rows="5">{esc(prompt)}</textarea>
<button type="button" id="copy-tutor-prompt">Copy tutor prompt</button>
<span id="tutor-copy-status" role="status" aria-live="polite"></span>
''')
parts=[f'<p id="tutor-materials-version">Materials version: <strong>{version}</strong></p>', '<h4>Reference index</h4><ul>']
for i,f in enumerate(manifest['files'],1):
    title=(f['group']+' — ' if f['group'] else '')+f['title'].replace('Assginment','Assignment')
    parts.append(f'<li><a href="#tutor-reference-{i}">{esc(title)}</a> · <a href="{esc(f['web_text_url'])}?v={revision}">Read text</a></li>')
parts+=['</ul>','<details class="tutor-reference" id="tutor-web-instructions" open><summary>Tutor instructions</summary><pre>'+esc(instructions)+'</pre></details>']
for i,(f,text) in enumerate(zip(manifest['files'],texts),1):
    title=(f['group']+' — ' if f['group'] else '')+f['title'].replace('Assginment','Assignment')
    parts.append(f'<details class="tutor-reference" id="tutor-reference-{i}"><summary>{esc(title)}</summary><p><a href="{esc(f["url"])}" target="_blank" rel="noopener noreferrer">Original document</a></p><pre>{esc(text)}</pre></details>')
(OUT/'references.html').write_text('\n'.join(parts)+'\n')
(ASSETS/'START_TUTOR.txt').write_text(prompt.rstrip()+'\n')
(ASSETS/'web-tutor-version.json').write_text(json.dumps({'version':version,'revision':revision,'reference_count':len(texts),'page_url':URL,'start_url':start_url},indent=2)+'\n')
assert len(texts)==len(manifest['files'])
print('Generated inline tutor:',version,'references:',len(texts))
