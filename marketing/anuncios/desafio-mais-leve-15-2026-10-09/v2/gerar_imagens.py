import asyncio, sys, pathlib
from playwright.async_api import async_playwright
OUT = sys.argv[1]
import base64
FD = pathlib.Path(sys.argv[2])
def F64(n): return 'data:font/ttf;base64,'+base64.b64encode((FD/n).read_bytes()).decode()
CSS = f"""
@font-face{{font-family:Bric;src:url('{F64("BricolageGrotesque-Bold.ttf")}')}}
@font-face{{font-family:BricR;src:url('{F64("BricolageGrotesque-Regular.ttf")}')}}
@font-face{{font-family:Inst;src:url('{F64("InstrumentSans-Regular.ttf")}')}}
@font-face{{font-family:InstB;src:url('{F64("InstrumentSans-Bold.ttf")}')}}
@font-face{{font-family:Hand;src:url('{F64("NothingYouCouldDo-Regular.ttf")}')}}
*{{margin:0;box-sizing:border-box}}
body{{width:@@W@@px;height:@@H@@px;overflow:hidden;position:relative;font-family:Inst;color:#2a1a20;
background-color:#fff;background-image:linear-gradient(#cfe0ee 1.5px,transparent 1.5px),linear-gradient(90deg,#cfe0ee 1.5px,transparent 1.5px);background-size:54px 54px;background-position:-1px -1px}}
.t{{font-family:Bric;color:#7A1F3D;letter-spacing:-2px;line-height:.92}}
.h{{font-family:Hand;color:#2E5E3A}}
.cta{{position:absolute;left:80px;bottom:80px;font-family:InstB;font-size:34px;background:#2E5E3A;color:#fff;padding:22px 38px;border-radius:12px}}
.marca{{position:absolute;right:80px;bottom:96px;font-family:InstB;font-size:26px;color:#7A1F3D}}
"""
def page(w,h,body): return f"<html><head><style>{CSS.replace("@@W@@",str(w)).replace("@@H@@",str(h))}</style></head><body>{body}</body></html>"

check = '<svg width="70" height="70" viewBox="0 0 70 70"><path d="M10 38 L28 56 L62 12" fill="none" stroke="#2E5E3A" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/></svg>'
boxes = ""
for i in range(1,16):
    inner = check if i<=6 else f'<span style="font-family:Bric;font-size:34px;color:#b9c9d6">{i}</span>'
    boxes += f'<div style="width:108px;height:108px;border:5px solid #7A1F3D;border-radius:10px;background:#fff;display:flex;align-items:center;justify-content:center;transform:rotate({(i*37%7-3)*0.6}deg)">{inner}</div>'

pecas = {
"01-capa-produto": (1080,1080, """
<div style="position:absolute;left:80px;top:96px;font-family:InstB;font-size:30px;color:#2E5E3A">Desafio de 15 dias</div>
<div class="t" style="position:absolute;left:72px;top:200px;font-size:250px">Mais<br>leve</div>
<svg style="position:absolute;left:520px;top:600px" width="500" height="230" viewBox="-20 0 470 230" preserveAspectRatio="none" ><path d="M30 120 C 20 40, 380 10, 405 100 C 425 190, 90 225, 40 150 C 25 125, 60 70, 140 55" fill="none" stroke="#F2992E" stroke-width="10" stroke-linecap="round"/></svg>
<div class="t" style="position:absolute;left:600px;top:655px;font-size:112px;color:#2E5E3A">15 dias</div>
<div class="h" style="position:absolute;left:80px;top:850px;font-size:54px;line-height:1.3">prato, passo e pausa<br><span style="color:#7A1F3D">cardápio pronto + 15 min por dia</span></div>
"""),
"02-anuncio-quarta-feira": (1080,1350, """
<div style="position:absolute;left:80px;top:90px;display:flex;gap:18px">
""" + "".join(f'<div style="width:168px;height:220px;background:#fff;border:4px solid #2a1a20;border-radius:10px;padding:16px"><div style="font-family:InstB;font-size:28px">{d}</div><div class="h" style="font-size:44px;margin-top:38px;color:{c}">{n}</div></div>' for d,n,c in [("seg","dieta!","#2E5E3A"),("ter","dieta","#2E5E3A"),("qua","...","#7A1F3D"),("qui","",""),("sex","","")]) + """
</div>
<svg style="position:absolute;left:460px;top:150px" width="190" height="180" viewBox="0 0 190 180"><path d="M20 20 L170 160 M170 20 L20 160" stroke="#F2992E" stroke-width="14" stroke-linecap="round"/></svg>
<div class="t" style="position:absolute;left:76px;top:420px;font-size:132px">A dieta que<br>acaba na<br>quarta-feira</div>
<div style="position:absolute;left:80px;top:880px;font-size:42px;line-height:1.35;width:900px">Começar cortando tudo não dura.<br><b style="font-family:InstB;color:#2E5E3A">15 dias com comida normal de casa.</b></div>
<div class="cta">Saiba mais</div><div class="marca">Desafio Mais Leve</div>
"""),
"03-anuncio-3p": (1080,1350, """
<div class="t" style="position:absolute;left:76px;top:90px;font-size:96px">O método<br>em 3 passos</div>
""" + "".join(f'''<div style="position:absolute;left:{x}px;top:{y}px;width:820px;height:230px;background:{bg};transform:rotate({r}deg);padding:34px 44px;box-shadow:0 18px 30px -18px rgba(60,20,30,.45)">
<div style="font-family:Bric;font-size:92px;color:{fg};line-height:1">{t}</div><div class="h" style="font-size:42px;color:#2a1a20;margin-top:10px">{s}</div></div>''' for x,y,r,bg,fg,t,s in [
 (90,370,-2,"#FBD38D","#7A1F3D","Prato","comida normal, cardápio pronto"),
 (170,640,1.5,"#CDE6C8","#2E5E3A","Passo","15 minutos de movimento em casa"),
 (100,910,-1,"#F6C6D3","#7A1F3D","Pausa","3 truques pra fome da noite")]) + """
<div class="marca" style="bottom:70px">Desafio Mais Leve · 15 dias</div>
"""),
"04-anuncio-15min": (1080,1350, f"""
<div class="t" style="position:absolute;left:76px;top:90px;font-size:112px">15 minutos<br>por dia, na<br>sala de casa</div>
<div style="position:absolute;left:105px;top:520px;display:grid;grid-template-columns:repeat(5,108px);gap:52px 60px">{boxes}</div>
<div class="h" style="position:absolute;left:600px;top:425px;font-size:60px;color:#F2992E;transform:rotate(-6deg)">dia 6 de 15!</div>
<div style="position:absolute;left:80px;top:1000px;font-size:40px;line-height:1.35">Sem academia e sem equipamento.<br><b style="font-family:InstB;color:#2E5E3A">Um checklist pra marcar cada dia.</b></div>
<div class="cta">Saiba mais</div><div class="marca">Desafio Mais Leve</div>
"""),
}
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for nome,(w,h,body) in pecas.items():
            pg = await b.new_page(viewport={"width":w,"height":h})
            await pg.set_content(page(w,h,body)); await pg.wait_for_timeout(800)
            await pg.screenshot(path=f"{OUT}/{nome}.png"); print("ok",nome)
        await b.close()
asyncio.run(main())
