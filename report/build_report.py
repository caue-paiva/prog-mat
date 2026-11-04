"""Renderiza relatorio.md em PDF. Requer reportlab e fonte DejaVu Sans."""
from pathlib import Path
import re
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT=Path(__file__).resolve().parent
fontdir=Path('/usr/share/fonts/truetype/dejavu')
if fontdir.exists():
    pdfmetrics.registerFont(TTFont('Body',str(fontdir/'DejaVuSans.ttf')))
    pdfmetrics.registerFont(TTFont('BodyBold',str(fontdir/'DejaVuSans-Bold.ttf')))
    pdfmetrics.registerFontFamily('Body',normal='Body',bold='BodyBold',italic='Body',boldItalic='BodyBold')
else:
    # O relatório usa caracteres latinos e notação de índices em texto.
    pdfmetrics.registerFontFamily('Helvetica',normal='Helvetica',bold='Helvetica-Bold')
FONT='Body' if fontdir.exists() else 'Helvetica'
BOLD='BodyBold' if fontdir.exists() else 'Helvetica-Bold'
styles=getSampleStyleSheet()
styles.add(ParagraphStyle('Text',fontName=FONT,fontSize=9.3,leading=14,spaceAfter=7,textColor=colors.HexColor('#233246')))
styles.add(ParagraphStyle('TitleCustom',fontName=BOLD,fontSize=22,leading=27,spaceAfter=15,textColor=colors.HexColor('#163c51')))
styles.add(ParagraphStyle('HeadingCustom',fontName=BOLD,fontSize=14,leading=18,spaceBefore=16,spaceAfter=9,keepWithNext=True,textColor=colors.HexColor('#12576b')))
styles.add(ParagraphStyle('SubCustom',fontName=BOLD,fontSize=10.5,leading=15,spaceBefore=9,spaceAfter=6,keepWithNext=True))
styles.add(ParagraphStyle('Cell',fontName=FONT,fontSize=7.3,leading=10))


def markup(s):
    s=escape(s)
    s=re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',s)
    return s


def footer(c,doc):
    c.setStrokeColor(colors.HexColor('#ccdbe0'));c.line(43,41,552,41)
    c.setFont(FONT,8);c.setFillColor(colors.HexColor('#516270'))
    c.drawString(43,28,'SME 0110 | Armazenamento de recursos | 04/11/2026')
    c.drawRightString(552,28,str(doc.page))


def build():
    lines=(ROOT/'relatorio.md').read_text().splitlines();story=[];i=0
    while i<len(lines):
        line=lines[i].strip();i+=1
        if not line:continue
        if line.startswith('|'):
            rows=[]
            while True:
                if not re.fullmatch(r'[| :\-]+',line):
                    rows.append([Paragraph(markup(s.strip()),styles['Cell']) for s in line.strip('|').split('|')])
                if i>=len(lines) or not lines[i].strip().startswith('|'):break
                line=lines[i].strip();i+=1
            cols=len(rows[0]);width=509/cols
            t=Table(rows,colWidths=[width]*cols,repeatRows=1,hAlign='LEFT')
            t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#d9edf1')),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.whitesmoke,colors.white]),('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),('LINEBELOW',(0,0),(-1,0),.6,colors.HexColor('#83a7b0'))]))
            story.extend([t,Spacer(1,9)])
        elif line.startswith('# '):story.append(Paragraph(markup(line[2:]),styles['TitleCustom']))
        elif line.startswith('## '):story.append(Paragraph(markup(line[3:]),styles['HeadingCustom']))
        elif line.startswith('### '):story.append(Paragraph(markup(line[4:]),styles['SubCustom']))
        else:story.append(Paragraph(markup(line),styles['Text']))
    SimpleDocTemplate(str(ROOT/'relatorio.pdf'),pagesize=(595.28,841.89),rightMargin=43,leftMargin=43,topMargin=43,bottomMargin=55,title='Otimização de Armazenamento de Recursos',author='Projeto SME 0110').build(story,onFirstPage=footer,onLaterPages=footer)

if __name__=='__main__':build()
