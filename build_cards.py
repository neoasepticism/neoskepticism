#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Neo-Skepticism 개념 카드덱 생성기 → card.html.  실행: python3 build_cards.py"""
def svg(inner): return '<svg viewBox="0 0 100 100" aria-hidden="true">'+inner+'</svg>'
G={}
G['overgrowth']=svg('<g fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"><rect x="16" y="30" width="24" height="11" rx="5.5"/><rect x="46" y="40" width="24" height="11" rx="5.5"/><rect x="26" y="54" width="24" height="11" rx="5.5"/><rect x="56" y="60" width="20" height="10" rx="5"/><path d="M74 26 l7 6 -7 6"/></g>')
G['overgrowth_f']=svg('<g fill="none" stroke="currentColor" stroke-width="3"><circle cx="34" cy="40" r="10"/><circle cx="54" cy="34" r="7"/><circle cx="60" cy="56" r="11"/><circle cx="38" cy="62" r="7"/><path d="M74 26 l7 6 -7 6" fill="none" stroke-linecap="round"/></g>')
G['vibrio']=svg('<g fill="none" stroke="currentColor" stroke-linecap="round"><path d="M32 62 Q34 34 62 34" stroke-width="9"/><path d="M62 34 q12 -3 16 -13 M63 40 q13 2 18 -6" stroke-width="2.4"/></g>')
G['rod']=svg('<g fill="none" stroke="currentColor" stroke-width="3.5"><rect x="26" y="42" width="44" height="17" rx="8.5"/><path d="M35 50 h26" stroke-width="1.6" opacity=".5"/></g>')
G['fusiform']=svg('<g fill="none" stroke="currentColor" stroke-width="3.2"><path d="M16 50 Q50 34 84 50 Q50 66 16 50 Z"/><path d="M50 40 V60" stroke-width="1.8" opacity=".55"/></g>')
G['coccobac']=svg('<g fill="none" stroke="currentColor" stroke-width="3.2"><rect x="30" y="40" width="20" height="13" rx="6.5"/><rect x="50" y="52" width="20" height="13" rx="6.5"/><path d="M30 40 l-5 -5 M50 40 l4 -6 M70 52 l6 -3" stroke-width="2" stroke-linecap="round" opacity=".6"/></g>')
G['cluster']=svg('<g fill="none" stroke="currentColor" stroke-width="3"><circle cx="40" cy="38" r="9"/><circle cx="56" cy="36" r="9"/><circle cx="48" cy="50" r="9"/><circle cx="62" cy="50" r="9"/><circle cx="42" cy="62" r="9"/><circle cx="58" cy="64" r="9"/></g>')
G['pseudo']=svg('<g fill="none" stroke="currentColor" stroke-width="3"><ellipse cx="30" cy="64" rx="10" ry="8"/><ellipse cx="48" cy="52" rx="10" ry="8"/><ellipse cx="66" cy="40" rx="10" ry="8"/><ellipse cx="80" cy="30" rx="6.5" ry="5.5"/></g>')
G['yeast']=svg('<g fill="none" stroke="currentColor" stroke-width="3.2"><circle cx="44" cy="56" r="18"/><circle cx="68" cy="38" r="10"/><path d="M57 45 l4 4" stroke-width="2" opacity=".5"/></g>')
G['malassezia']=svg('<g fill="none" stroke="currentColor" stroke-width="3.2"><circle cx="45" cy="56" r="17"/><path d="M57 45 q5 -1 5 -6 q0 -5 -5 -6" stroke-width="2.6"/><circle cx="66" cy="33" r="8.5"/></g>')
G['h2s']=svg('<g fill="none" stroke="currentColor"><path d="M30 62 L50 44 L70 62" stroke-width="3"/><circle cx="50" cy="44" r="8" fill="currentColor" stroke="none"/><circle cx="30" cy="62" r="5"/><circle cx="70" cy="62" r="5"/></g><text x="50" y="30" text-anchor="middle" font-size="14" font-family="monospace" fill="currentColor">S</text>')
G['ch3sh']=svg('<g fill="none" stroke="currentColor"><path d="M22 60 L42 48 L62 60 L82 48" stroke-width="3"/><circle cx="42" cy="48" r="6"/><circle cx="62" cy="60" r="6"/><circle cx="82" cy="48" r="8" fill="currentColor" stroke="none"/><path d="M42 48 l-4 -10 M42 48 l6 -9" stroke-width="2" opacity=".6"/></g><text x="82" y="38" text-anchor="middle" font-size="12" font-family="monospace" fill="currentColor">S</text>')
G['h2']=svg('<g fill="none" stroke="currentColor" stroke-width="3"><path d="M38 50 H62"/><circle cx="38" cy="50" r="9"/><circle cx="62" cy="50" r="9"/></g><text x="50" y="30" text-anchor="middle" font-size="12" font-family="monospace" fill="currentColor">H₂</text>')
G['co2']=svg('<g fill="none" stroke="currentColor" stroke-width="2.6"><path d="M34 46 H46 M34 54 H46 M54 46 H66 M54 54 H66"/></g><g stroke="currentColor" stroke-width="3" fill="none"><circle cx="24" cy="50" r="7"/><circle cx="76" cy="50" r="7"/></g><circle cx="50" cy="50" r="9" fill="currentColor" stroke="none"/><text x="50" y="30" text-anchor="middle" font-size="11" font-family="monospace" fill="currentColor">CO₂</text>')
G['fiber']=svg('<g fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"><path d="M20 38 Q50 60 80 38"/><path d="M20 52 Q50 74 80 52"/><path d="M20 66 Q50 44 80 66"/></g>')
G['garlic']=svg('<g fill="none" stroke="currentColor" stroke-width="3"><path d="M30 56 Q30 36 50 36 Q70 36 70 56 Q70 72 50 72 Q30 72 30 56 Z"/><path d="M42 38 Q42 58 43 70 M50 36 V72 M58 38 Q58 58 57 70" stroke-width="2" opacity=".6"/><path d="M50 36 Q47 26 50 20 Q53 26 50 36" stroke-width="2.4"/></g>')
G['onion']=svg('<g fill="none" stroke="currentColor" stroke-width="3"><path d="M28 56 Q28 34 50 34 Q72 34 72 56 Q72 74 50 74 Q28 74 28 56 Z"/><ellipse cx="50" cy="55" rx="11" ry="15" stroke-width="2" opacity=".55"/><path d="M50 34 q-4 -8 -1 -14 M50 34 q4 -8 1 -14" stroke-width="2.4"/></g>')
G['roll']=svg('<g fill="none" stroke="currentColor"><circle cx="50" cy="50" r="25" stroke-width="4"/><circle cx="50" cy="50" r="20" stroke-width="2" opacity=".5"/><circle cx="50" cy="50" r="7" stroke-width="2.6"/><circle cx="50" cy="38" r="3.2" fill="currentColor" stroke="none"/><circle cx="61" cy="55" r="3.2" fill="currentColor" stroke="none"/><circle cx="40" cy="58" r="3.2" fill="currentColor" stroke="none"/></g>')
G['leaf']=svg('<g fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round"><path d="M50 20 C40 30 30 34 34 50 C36 62 30 66 34 74 C48 72 46 78 50 80 C54 78 52 72 66 74 C70 66 64 62 66 50 C70 34 60 30 50 20 Z"/><path d="M50 30 V74" stroke-width="2" opacity=".55"/><path d="M50 46 L40 42 M50 56 L60 52 M50 40 L58 36" stroke-width="1.8" opacity=".5"/></g>')
G['capsule']=svg('<g fill="none" stroke="currentColor" stroke-width="3"><rect x="24" y="38" width="52" height="24" rx="12"/><path d="M50 38 V62" stroke-width="2"/><circle cx="37" cy="50" r="3.4" fill="currentColor" stroke="none"/><circle cx="61" cy="47" r="3.4" fill="currentColor" stroke="none"/><circle cx="63" cy="55" r="2.6" fill="currentColor" stroke="none"/></g>')
G['grain']=svg('<g fill="none" stroke="currentColor" stroke-width="2.6"><path d="M50 24 Q58 24 58 40 Q58 56 50 56 Q42 56 42 40 Q42 24 50 24 Z"/><path d="M50 26 V54" stroke-width="1.6" opacity=".55"/><path d="M34 44 Q40 44 40 58 Q40 70 34 70 Q28 70 28 58 Q28 44 34 44 Z"/><path d="M34 46 V68" stroke-width="1.4" opacity=".55"/><path d="M66 44 Q72 44 72 58 Q72 70 66 70 Q60 70 60 58 Q60 44 66 44 Z"/><path d="M66 46 V68" stroke-width="1.4" opacity=".55"/></g>')
G['jar']=svg('<g fill="none" stroke="currentColor" stroke-width="3"><path d="M32 42 Q29 70 50 74 Q71 70 68 42 Z"/><path d="M35 42 Q50 34 65 42" stroke-width="2.6"/></g><g fill="currentColor"><circle cx="44" cy="56" r="3"/><circle cx="56" cy="61" r="2.4"/><circle cx="51" cy="49" r="2"/></g>')
G['choline']=svg('<g fill="none" stroke="currentColor" stroke-width="3"><path d="M20 58 L38 48 L56 58 L72 48"/></g><circle cx="72" cy="48" r="8" fill="currentColor" stroke="none"/><g fill="none" stroke="currentColor" stroke-width="2.4"><path d="M72 48 l8 -8 M72 48 l10 4"/></g><text x="72" y="35" text-anchor="middle" font-size="11" font-family="monospace" fill="currentColor">N</text>')
G['ecoli']=svg('<g fill="none" stroke="currentColor" stroke-width="3.2"><rect x="32" y="42" width="36" height="16" rx="8"/></g><g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M32 46 q-9 -3 -15 0 M32 54 q-9 3 -15 6 M68 46 q9 -3 15 0 M68 54 q9 3 15 6 M46 42 q-2 -9 -6 -13 M56 58 q2 9 6 13"/></g>')
G['rodchain']=svg('<g fill="none" stroke="currentColor" stroke-width="3"><rect x="14" y="44" width="20" height="13" rx="6.5"/><rect x="40" y="44" width="20" height="13" rx="6.5"/><rect x="66" y="44" width="20" height="13" rx="6.5"/></g>')
G['indole']=svg('<g fill="none" stroke="currentColor" stroke-width="2.8" stroke-linejoin="round"><path d="M20 42 L20 60 L36 69 L52 60 L52 42 L36 33 Z"/><path d="M52 42 L52 60 L70 65 L79 51 L70 37 Z"/></g><text x="72" y="55" text-anchor="middle" font-size="11" font-family="monospace" fill="currentColor">N</text>')
G['tma']=svg('<circle cx="50" cy="50" r="8" fill="currentColor" stroke="none"/><g fill="none" stroke="currentColor" stroke-width="3"><path d="M50 50 L28 38 M50 50 L28 62 M50 50 L74 50"/></g><g fill="none" stroke="currentColor" stroke-width="2.6"><circle cx="28" cy="38" r="5"/><circle cx="28" cy="62" r="5"/><circle cx="74" cy="50" r="5"/></g><text x="50" y="40" text-anchor="middle" font-size="11" font-family="monospace" fill="currentColor">N</text>')
G['histamine']=svg('<g fill="none" stroke="currentColor" stroke-width="2.8" stroke-linejoin="round"><path d="M20 44 L20 60 L36 66 L46 52 L36 38 Z"/><path d="M46 52 L60 45 L72 53 L84 46"/></g><g fill="none" stroke="currentColor" stroke-width="2.4"><circle cx="84" cy="46" r="5"/></g>')
G['glp1']=svg('<g fill="none" stroke="currentColor" stroke-width="3"><rect x="24" y="42" width="52" height="22" rx="11"/></g><circle cx="63" cy="53" r="7.5" fill="currentColor" stroke="none"/><g fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M78 40 q6 -4 4 -12 M84 46 q7 -2 9 -9"/></g>')
G['brain']=svg('<g fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round"><path d="M30 54 Q26 36 44 32 Q54 24 66 32 Q80 34 78 50 Q80 64 66 68 Q54 76 42 70 Q30 68 30 54 Z"/><path d="M44 40 Q50 46 44 52 M58 36 Q64 44 56 50" stroke-width="1.8" opacity=".55"/></g><path d="M46 58 Q54 52 62 58 Q58 68 54 66 Q48 68 46 58 Z" fill="currentColor" stroke="none" opacity=".4"/>')
G['biofilm']=svg('<g fill="none" stroke="currentColor" stroke-width="3"><path d="M18 60 Q50 36 82 60" stroke-width="2.6"/><path d="M18 66 H82"/></g><g fill="none" stroke="currentColor" stroke-width="2.6"><circle cx="34" cy="61" r="4"/><rect x="45" y="57" width="12" height="8" rx="4"/><circle cx="66" cy="61" r="4"/></g>')
G['mito']=svg('<g fill="none" stroke="currentColor" stroke-width="3"><ellipse cx="46" cy="52" rx="28" ry="16"/><path d="M26 52 Q34 42 40 52 Q46 62 52 52 Q58 42 64 52" stroke-width="2.2"/></g><g fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round"><path d="M66 34 L84 52 M84 34 L66 52"/></g>')
G['gutbrain']=svg('<g fill="none" stroke="currentColor" stroke-width="2.8" stroke-linejoin="round"><path d="M40 22 Q32 24 34 34 Q48 32 54 25 Q52 18 40 22 Z"/><path d="M45 40 V52" stroke-width="2.4"/><path d="M30 60 Q50 50 70 60 Q64 76 50 73 Q36 76 30 60 Z"/><path d="M38 64 Q50 70 62 64" stroke-width="1.8" opacity=".55"/></g>')
G['analyzer']=svg('<g fill="none" stroke="currentColor" stroke-width="3"><rect x="26" y="34" width="40" height="34" rx="6"/><path d="M38 52 A11 11 0 0 1 60 52" stroke-width="2.4"/><path d="M49 52 L57 44" stroke-width="2.4" stroke-linecap="round"/><rect x="66" y="45" width="16" height="11" rx="3.5"/></g><g fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M82 50 q6 -3 10 0"/></g>')
G['ricebowl']=svg('<g fill="none" stroke="currentColor" stroke-width="3"><path d="M26 54 Q26 71 50 73 Q74 71 74 54 Z"/><path d="M31 54 Q50 41 69 54" stroke-width="2.6"/></g><g fill="currentColor"><circle cx="44" cy="52" r="2.2"/><circle cx="54" cy="50" r="2.2"/><circle cx="50" cy="57" r="2.2"/></g><g fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" opacity=".7"><path d="M44 40 q-3 -7 1 -12 M56 40 q3 -7 -1 -12"/></g>')
G['antibiotic']=svg('<g fill="none" stroke="currentColor" stroke-width="3"><rect x="20" y="40" width="34" height="17" rx="8.5" transform="rotate(-18 37 48)"/><path d="M31 37 L44 55" stroke-width="2" opacity=".6"/></g><g fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round"><circle cx="70" cy="58" r="9"/><path d="M64 52 l12 12 M76 52 l-12 12"/></g>')
G['steam']=svg('<g fill="none" stroke="currentColor" stroke-width="3"><path d="M28 58 Q30 72 50 74 Q70 72 72 58 Z"/><path d="M28 58 H72" stroke-width="2.6"/></g><g fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" opacity=".8"><path d="M40 48 q-4 -6 0 -11 q4 -5 0 -11 M50 46 q-4 -6 0 -11 q4 -5 0 -11 M60 48 q-4 -6 0 -11 q4 -5 0 -11"/></g>')
G['tab_round']=svg('<g fill="none" stroke="currentColor" stroke-width="3.2"><circle cx="50" cy="50" r="22"/><path d="M32 50 H68"/></g>')
G['tab_oval']=svg('<g fill="none" stroke="currentColor" stroke-width="3.2"><ellipse cx="50" cy="50" rx="26" ry="15"/><path d="M50 36 V64" stroke-width="2" opacity=".5"/></g>')
G['cap_plain']=svg('<g fill="none" stroke="currentColor" stroke-width="3.2"><rect x="24" y="40" width="52" height="20" rx="10"/><path d="M50 40 V60" stroke-width="2" opacity=".5"/></g>')
G['cap_two']=svg('<g stroke="currentColor" stroke-width="3.2"><rect x="24" y="40" width="52" height="20" rx="10" fill="none"/><path d="M34 40 h16 v20 h-16 a10 10 0 0 1 0 -20 Z" fill="currentColor" opacity=".2" stroke="none"/><path d="M50 40 V60" fill="none" stroke-width="2"/></g>')
G['cap_line']=svg('<g fill="none" stroke="currentColor" stroke-width="3.2"><rect x="24" y="40" width="52" height="20" rx="10"/><path d="M34 45 V55 M42 45 V55 M50 45 V55" stroke-width="1.8" opacity=".5"/></g>')
G['tab_gut']=svg('<g fill="none" stroke="currentColor" stroke-width="3"><ellipse cx="50" cy="38" rx="20" ry="12"/><path d="M34 38 H66" opacity=".5" stroke-width="1.8"/><path d="M30 66 Q50 56 70 66 Q64 78 50 76 Q36 78 30 66 Z"/><path d="M38 69 Q50 74 62 69" stroke-width="1.6" opacity=".55"/></g>')
G['cap_fungi']=svg('<g fill="none" stroke="currentColor" stroke-width="3"><rect x="18" y="38" width="42" height="18" rx="9"/><path d="M39 38 V56" stroke-width="1.8" opacity=".5"/></g><g fill="none" stroke="currentColor" stroke-width="2.4"><circle cx="72" cy="62" r="6"/><circle cx="80" cy="52" r="4.5"/><path d="M64 68 L80 54" stroke-width="2.6" stroke-linecap="round"/></g>')
G['cap_spore']=svg('<g fill="none" stroke="currentColor" stroke-width="3"><rect x="18" y="38" width="42" height="18" rx="9"/><path d="M39 38 V56" stroke-width="1.8" opacity=".5"/></g><g fill="none" stroke="currentColor" stroke-width="2.4"><circle cx="74" cy="60" r="8"/></g><g fill="currentColor"><circle cx="71" cy="58" r="1.6"/><circle cx="77" cy="61" r="1.6"/><circle cx="74" cy="63" r="1.6"/></g><path d="M64 70 L84 50" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" fill="none"/>')
G['tab_fungi']=svg('<g fill="none" stroke="currentColor" stroke-width="3.2"><circle cx="42" cy="46" r="17"/><path d="M27 46 H57" stroke-width="2.4"/></g><g fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M62 66 Q68 58 66 50 M68 66 Q74 60 76 52"/><path d="M58 68 L80 54" stroke-width="2.6"/></g>')
# ---- symptom glyphs ----
G['colon']=svg('<g fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round"><path d="M24 40 Q24 28 38 28 L56 28 Q70 28 70 42 Q70 54 56 54 L40 54 Q30 54 30 62 Q30 72 42 72 L64 72"/></g><circle cx="60" cy="40" r="10" fill="currentColor" stroke="none" opacity=".45"/><circle cx="60" cy="40" r="12" fill="none" stroke="currentColor" stroke-width="2.4"/>')
G['mouth']=svg('<g fill="none" stroke="currentColor" stroke-width="3"><path d="M26 50 Q50 36 74 50 Q50 66 26 50 Z"/><path d="M35 52 Q50 59 65 52"/></g><g fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" opacity=".7"><path d="M50 34 q6 -6 2 -12 M63 36 q6 -5 3 -11"/></g>')
G['rash']=svg('<g fill="none" stroke="currentColor" stroke-width="3"><rect x="26" y="30" width="48" height="40" rx="11"/></g><g fill="currentColor"><circle cx="40" cy="44" r="3.6"/><circle cx="56" cy="40" r="3"/><circle cx="50" cy="55" r="3.6"/><circle cx="63" cy="57" r="2.6"/><circle cx="36" cy="58" r="2.6"/></g>')
G['nose']=svg('<g fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round"><path d="M54 24 Q47 44 41 54 Q38 60 45 62 Q52 64 56 59"/><path d="M41 56 Q34 56 34 62 Q34 67 41 66"/></g><g fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" opacity=".7"><path d="M44 72 v8 M53 72 v6"/></g>')
G['fog']=svg('<g fill="none" stroke="currentColor" stroke-width="2.8" stroke-linejoin="round" opacity=".85"><path d="M32 44 Q28 30 44 28 Q54 22 64 30 Q76 32 74 46"/></g><g fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"><path d="M28 54 H72 M32 62 H68 M36 70 H64"/></g>')
G['venus']=svg('<g fill="none" stroke="currentColor" stroke-width="3.4"><circle cx="50" cy="40" r="15"/><path d="M50 55 V78 M39 68 H61"/></g>')
G['cycle']=svg('<g fill="none" stroke="currentColor" stroke-width="3"><circle cx="50" cy="50" r="24" stroke-dasharray="3 6" opacity=".55"/></g><path d="M60 33 A18 18 0 1 0 60 67 A22 22 0 0 1 60 33 Z" fill="currentColor" stroke="none" opacity=".55"/>')
G['raincloud']=svg('<g fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round"><path d="M32 50 Q25 50 25 43 Q25 34 36 34 Q38 26 48 26 Q59 26 61 35 Q73 35 73 45 Q73 51 65 51 Z"/></g><g fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" opacity=".75"><path d="M38 58 L34 68 M50 58 L46 70 M62 58 L58 68"/></g>')
G['ch4']=svg('<circle cx="50" cy="50" r="8" fill="currentColor" stroke="none"/><g fill="none" stroke="currentColor" stroke-width="3"><path d="M50 50 L30 38 M50 50 L30 62 M50 50 L70 38 M50 50 L70 62"/></g><g fill="none" stroke="currentColor" stroke-width="2.4"><circle cx="30" cy="38" r="5"/><circle cx="30" cy="62" r="5"/><circle cx="70" cy="38" r="5"/><circle cx="70" cy="62" r="5"/></g>')
G['leaky']=svg('<g fill="none" stroke="currentColor" stroke-width="3"><path d="M20 42 H80 M20 58 H80"/></g><g fill="none" stroke="currentColor" stroke-width="3" stroke-dasharray="9 7"><path d="M20 50 H80"/></g><g fill="currentColor"><circle cx="42" cy="50" r="3"/><circle cx="58" cy="50" r="2.6"/><circle cx="50" cy="50" r="2.2"/></g>')

# ---- data: (name, sci, glyph, [cls,] badge, desc, meta) ----
STAGE=[
 ("SIBO","Small Intestinal Bacterial Overgrowth","overgrowth","과증식 상태","소장에 세균이 과하게 늘어난 상태. 복부팽만·가스·설사·영양흡수 저하의 배경.","→ 무대: 세균이 자라는 곳"),
 ("SIFO","Small Intestinal Fungal Overgrowth","overgrowth_f","과증식 상태","세균이 아니라 진균(효모·곰팡이)이 소장에서 과증식. SIBO와 증상이 겹칩니다.","→ 무대: 곰팡이 버전"),
]
SUB=[
 ("섬유질","Fiber","fiber","기질 · 먹이","장에서 다 흡수되지 않고 대장으로 내려가 발효의 재료가 됩니다.",'명분 <s>좋은 균의 먹이</s> → 실체: 발효 기질'),
 ("통곡물·잡곡","Whole grains","grain","기질 · 먹이","저속노화 식단으로 권장되지만, 난소화성 기질이 발효 시간을 늘립니다.",'명분 <s>저속노화</s> → 실체: 발효 시간 연장'),
 ("마늘","Garlic","garlic","기질 · 먹이","식물 황(黃)의 대표 공급원. 호흡가스 분석에서 가장 친염증성인 것 중 하나.",'명분 <s>항염 · 면역</s> → 실체: 식물 황 공급'),
 ("양파","Onion","onion","기질 · 먹이","황과 프럭탄(난소화성 당)을 함께 공급해 장내 발효를 키웁니다.",'명분 <s>항산화</s> → 실체: 황 · 프럭탄'),
 ("김치·발효식품","Fermented foods","jar","기질 · 먹이","외부 세균·진균을 몸에 직접 투입하는 셈. 한국 식단의 사각지대.",'명분 <s>프로바이오틱</s> → 실체: 외부 균 투입'),
 ("김밥","Gimbap","roll","기질 · 먹이","생채소·김·밥이 뭉친 상온 보관 한 끼 — 여러 기질과 세균 노출이 한 번에.",'명분 <s>간편한 한 끼</s> → 실체: 기질 + 상온 세균'),
 ("상추","Lettuce","leaf","기질 · 먹이","생채소를 그대로 먹는 것은 세균을 직접 섭취하는 일이며, 알칼리성이 환경을 바꿉니다.",'명분 <s>생채소 · 다이어트</s> → 실체: 날 세균 · 알칼리'),
 ("프로바이오틱스","Probiotics","capsule","기질 · 먹이","'좋은 균'으로 팔리지만, 히스타민 생산균을 몸에 직접 투입하는 셈입니다.",'명분 <s>좋은 균 보충</s> → 실체: 히스타민 생산균'),
 ("콜린·카르니틴","Choline · Carnitine","choline","기질 · 먹이","계란·붉은 고기·생선에 풍부. 장내 세균이 이를 분해해 생선냄새(TMA)를 만듭니다.",'→ TMA(생선냄새)의 원료'),
]
MIC=[
 ("SRB","Sulfate-Reducing Bacteria · Desulfovibrio","vibrio","세균","황을 환원해 황화수소를 만드는 세균. 포만 호르몬 GLP-1까지 억제하는 핵심 용의자.","→ 만드는 것: H₂S · GLP-1 억제"),
 ("에거텔라","Eggerthella","rod","세균","황화수소 생산과 연결되는 장내 세균. 우울·양극성 패턴에서 지목.","→ 연결: 우울 · H₂S"),
 ("후소박테리움","Fusobacterium nucleatum","fusiform","세균","한 균이 세 얼굴 — 메틸메르캅탄(입냄새·불안)과 대장암에 모두 관여.","→ 만드는 것: 메틸메르캅탄"),
 ("진지발리스","Porphyromonas gingivalis","coccobac","세균","치주염의 대표균. 구취·잇몸병을 넘어 전신 염증과의 연결이 연구됩니다.","→ 자리: 잇몸 · 구강"),
 ("황색포도상구균","Staphylococcus aureus","cluster","세균","아토피 피부의 ~70%에서 검출. '다양성 부족'이 아니라 이 한 균의 과증식.","→ 결과: 아토피 · 피부염"),
 ("대장균","Escherichia coli","ecoli","세균","후소박테리움과 함께 불안·초조 패턴에서 지목되는 흔한 장내균.","→ 연결: 불안 · 메틸메르캅탄"),
 ("락토바실러스","Lactobacillus","rodchain","세균","'유산균'으로 팔리지만, 히스타민을 생산하고 드물게 균혈증을 일으킵니다.","→ 프로바이오틱의 실체"),
 ("칸디다","Candida","pseudo","진균 · 곰팡이","재발성 질염과 장 과증식의 주역. 가성균사를 뻗어 조직을 파고듭니다.","→ 결과: 재발성 감염"),
 ("효모","Yeast","yeast","진균 · 곰팡이","당을 발효시키는 미생물. SIFO의 핵심 — 몸 안에서 원치 않는 발효.","→ 무대: SIFO"),
 ("말라쎄지아","Malassezia","malassezia","진균 · 곰팡이","지루성 피부염·비듬의 방아쇠. 피부를 알칼리화시켜 포도상구균 악순환을 엽니다.","→ 결과: 지루성 · 비듬"),
]
GAS=[
 ("황화수소","H₂S · Hydrogen sulfide","h2s","가스 · 독소","썩은 계란 냄새. 시안화물과 같은 계열의 미토콘드리아 독성을 가집니다. SRB의 산물.","→ 독성: 세포 호흡 억제"),
 ("메틸메르캅탄","CH₃SH · Methyl mercaptan","ch3sh","가스 · 독소","마늘 호흡의 진짜 정체. 표준 검사가 놓치는 가스이며, 불안과 강하게 연결.","→ 검사가 놓침 · 불안"),
 ("인돌·스카톨","Indole · Skatole","indole","가스 · 독소","황이 아닌 악취 물질. VSC 측정기로는 '정상'인데 냄새는 심한 구취의 정체.","→ 검사가 놓침 · 대변 냄새"),
 ("트리메틸아민","TMA · Trimethylamine","tma","가스 · 독소","생선 썩는 냄새의 정체. 장내 세균이 콜린을 분해해 만들며, 저용량 항생제로 다스립니다.","→ 생선냄새증후군(TMAU)"),
 ("히스타민","Histamine","histamine","가스 · 독소","프로바이오틱·발효식품이 늘리는 물질. 두드러기·알러지성 두통·물 알러지의 기여자.","→ 결과: 알러지 · 두드러기"),
 ("수소","H₂ · Hydrogen","h2","가스 · 무취","발효로 나오는 흔한 무취 가스. SIBO 호흡검사의 기본 측정 대상.","→ 무취 · 발효 부산물"),
 ("이산화탄소","CO₂ · Carbon dioxide","co2","가스 · 무취","발효가 만드는 무취 가스. 가스·팽만감의 '부피'를 채웁니다.","→ 무취 · 팽만의 부피"),
 ("메탄","CH₄ · Methane","ch4","가스 · 무취","메탄생성 고세균이 만드는 무취 가스. 장운동을 늦춰 변비형 팽만과 연결됩니다.","→ 무취 · 변비형 · 장운동 지연"),
]
MECH=[
 ("GLP-1","Glucagon-like peptide-1","glp1","mech","기전 · 회로","식후 분비되어 포만감을 주고 충동을 진정시키는 스위치. SRB가 이걸 꺼버립니다.","→ 세균이 끄는 포만 스위치"),
 ("변연계","Limbic system","brain","mech","기전 · 회로","식욕·중독·감정의 중추. GLP-1이 꺼지면 도파민에 끌려다니는 '노예'가 됩니다.","→ 도파민 · 충동의 무대"),
 ("바이오필름","Biofilm","biofilm","mech","기전 · 회로","균이 스스로 만드는 끈끈한 막. 표면만 닦아선 안 잡히고, 제균이 어려운 이유.","→ 균이 숨는 막"),
 ("미토콘드리아 독성","Mitochondrial toxicity","mito","mech","기전 · 회로","황가스가 시안화물과 같은 방식으로 세포의 에너지 공장을 억제 → 피로·브레인포그.","→ 세포 호흡 억제"),
 ("장뇌축","Gut–brain axis","gutbrain","mech","기전 · 회로","장에서 만든 가스가 뇌와 감정 중추에 닿는 실제 경로. 은유가 아닙니다.","→ 장 → 뇌 실경로"),
 ("장누수","Leaky gut","leaky","mech","기전 · 회로","장벽의 조밀결합이 느슨해져 세균 산물이 혈류로 새는 상태. 저강도 전신 염증의 통로.","→ 장벽 투과 → 전신 염증"),
]
SX=[
 ("대장암","Colorectal cancer","colon","sx","결과 · 증상","후소박테리움이 FadA로 추동하는 것으로 연구되는 암. 젊은 층에서 증가하는 추세.","← 후소박테리움"),
 ("구취","Halitosis","mouth","sx","결과 · 증상","VSC·인돌 계열이 만드는 입냄새. 측정이 정상이어도 존재할 수 있습니다.","← 가스 · 세균"),
 ("피부염","Dermatitis","rash","sx","결과 · 증상","아토피·지루성·주사 — 황색포도상구균·말라쎄지아 과증식과 피부 알칼리화.","← 황포 · 말라쎄지아"),
 ("비염","Rhinitis","nose","sx","결과 · 증상","히스타민·알러지 반응과 연결되는 코 증상.","← 히스타민"),
 ("집중력 장애","Brain fog","fog","sx","결과 · 증상","황가스 재흡입으로 인한 뇌 안개·집중 저하·만성 피로.","← 가스 재흡입"),
 ("질염","Vaginitis","venus","sx","결과 · 증상","재발성 칸디다 질염 — 진균 과증식과 연결되는 흔한 여성 증상.","← 칸디다"),
 ("생리전 증후군","PMS","cycle","sx","결과 · 증상","호르몬 주기와 장내 상태가 겹쳐 나타나는 주기적 증상 패턴.","← 장내 상태"),
 ("우울증","Depression","raincloud","sx","결과 · 증상","에거텔라·황화수소와 연결이 연구되는 기분 저하.","← 에거텔라 · H₂S"),
]
FIX=[
 ("호흡가스 분석기","Breath gas analyzer","analyzer","fix","해법 · 도구","현대 웰니스 식단의 '거짓말 탐지기'. 표준 검사가 놓치는 황 가스를 직접 측정합니다.","★ 이 프레임의 심장"),
 ("흰쌀밥","White rice · Carni-rice","ricebowl","fix","해법 · 도구","난소화성 기질의 반대편. 발효를 덜 부르고 GLP-1이 정상 작동하는 탄수화물.","→ 기질의 반대편"),
 ("경험적 제균","Empirical antimicrobials","antibiotic","fix","해법 · 도구","냄새가 있다면 원인은 세균 — 측정이 안 돼도 경험적으로 다스립니다. 다수 성공.","→ 냄새 → 세균 → 치료"),
 ("뜨거운 음식","Hot, cooked food","steam","fix","해법 · 도구","날것·아이스의 반대. 세균 노출을 줄이는 디컨타미네이션의 기본.","→ 아이스 · 날것의 반대"),
]
DRUG=[
 ("메트로니다졸","Metronidazole","tab_round","drug","항생제","혐기성 세균과 원충의 표준 무기. 산소를 싫어하는 균(SRB 등)에 강합니다.","→ 표적: 혐기성 세균"),
 ("리팍시민","Rifaximin","tab_gut","drug","항생제","장에서 거의 흡수되지 않는 장 특화 항생제. SIBO의 표준 선택.","→ 표적: 장 국소 · SIBO"),
 ("시프로플록사신","Ciprofloxacin","cap_plain","drug","항생제","광범위 퀴놀론계. 그람음성균에 특히 강한 무기.","→ 표적: 그람음성균"),
 ("아목시실린/클라불란산","Amoxicillin/clavulanate","cap_two","drug","항생제","광범위 페니실린에 내성 차단제를 더한 조합. 폭넓게 씁니다.","→ 표적: 광범위"),
 ("독시사이클린","Doxycycline","cap_line","drug","항생제","테트라사이클린계. 광범위하면서 항염 효과도 갖습니다.","→ 표적: 광범위 · 항염"),
 ("클래리스로마이신","Clarithromycin","tab_oval","drug","항생제","마크로라이드계. 조직·세포 안으로 잘 파고들어 바이오필름에 유리.","→ 표적: 조직 침투"),
 ("플루코나졸","Fluconazole","cap_spore","drug","항진균제","칸디다 등 효모에 널리 쓰이는 대표 항진균제.","→ 표적: 칸디다 · 효모"),
 ("이트라코나졸","Itraconazole","cap_fungi","drug","항진균제","광범위 항진균제. 곰팡이·말라쎄지아까지 폭넓게.","→ 표적: 곰팡이 · 말라쎄지아"),
 ("테르비나핀","Terbinafine","tab_fungi","drug","항진균제","피부·손발톱 곰팡이의 대표 무기.","→ 표적: 피부 진균"),
]

# ---- 사진 아트 (art/): 카드 이름 → 파일명. 없는 카드는 SVG 글리프 유지 ----
IMG={
 'SIBO':'SIBO.jpg','SIFO':'SIFO.jpg','마늘':'garlic.jpg','양파':'onion.jpg',
 '김밥':'gimbap.jpg','상추':'lettuce.jpg','SRB':'SRB.jpg','에거텔라':'egerthella.jpg',
 '후소박테리움':'fusobacterium.jpg','진지발리스':'gingivalis.jpg','황색포도상구균':'staphylococcus.jpg',
 '칸디다':'candida.jpg','효모':'yeast.jpg','말라쎄지아':'malassezia.jpg',
 '황화수소':'h2s.jpg','메틸메르캅탄':'CH3SH.jpg','수소':'H2.jpg','이산화탄소':'CO2.jpg',
 'GLP-1':'GLP1.jpg','변연계':'limbic.jpg','바이오필름':'biofilm.jpg','미토콘드리아 독성':'mitochondrion.jpg',
 '장뇌축':'gut_brain_axis.jpg','대장암':'coloncancer.jpg','구취':'halitosis.jpg','피부염':'dermatitis.jpg',
 '비염':'rhinitis.jpg','집중력 장애':'attentiondeficit.jpg','질염':'vaginitis.jpg',
 '생리전 증후군':'PMS.jpg','우울증':'depression.jpg',
 '메탄':'CH4.jpg','장누수':'leakygut.jpg',
}
def cls_for(b):
    if '기질' in b: return 'sub'
    if '가스' in b: return 'gas'
    return ''
def cards(rows):
    o=''
    for r in rows:
        name,sci,gl,badge,desc,meta=r[0],r[1],r[2],r[-3],r[-2],r[-1]
        cls=r[3] if (len(r)==7 and r[3] in ('mech','fix','drug','sx')) else cls_for(badge)
        if name in IMG:
            glyph='<div class="pglyph img"><img src="art/'+IMG[name]+'" alt="'+name+'" loading="lazy"></div>'
        else:
            glyph='<div class="pglyph">'+G[gl]+'</div>'
        o+=('    <div class="pcard '+cls+'">\n      '+glyph+'\n'
            '      <div class="psci">'+sci+'</div>\n      <div class="pname">'+name+'</div>\n'
            '      <span class="pbadge">'+badge+'</span>\n      <p class="pdesc">'+desc+'</p>\n'
            '      <div class="pmeta">'+meta+'</div>\n    </div>\n')
    return o
def sec(eb,cls,h2,sub,rows):
    return ('<div class="sechead"><span class="eyebrow '+cls+'">'+eb+'</span><h2>'+h2+'</h2><p>'+sub+'</p></div>\n  <div class="deck">\n'+cards(rows)+'  </div>\n')

groups=[STAGE,SUB,MIC,GAS,MECH,SX,FIX,DRUG]
total=sum(len(x) for x in groups); T=str(total)
BODY=(
'<section><div class="wrap">\n'+sec('① 무대 · '+str(len(STAGE))+'장','','어디서 벌어지나','증상이 시작되는 장소 — 세균과 진균이 소장에서 과하게 늘어난 두 상태.',STAGE)+'</div></section>\n\n'
'<section class="alt"><div class="wrap">\n'+sec('② 먹이 · '+str(len(SUB))+'장','s','무엇이 키우나','"몸에 좋다"고 배운 것들이, 이 프레임에서는 세균의 먹이(기질)로 지목됩니다.',SUB)+'</div></section>\n\n'
'<section><div class="wrap">\n'+sec('③ 용의자 · '+str(len(MIC))+'장','','누가 자라나','흩어진 증상 뒤에서 반복해 등장하는 세균과 진균.',MIC)+'</div></section>\n\n'
'<section class="alt"><div class="wrap">\n'+sec('④ 산물 · '+str(len(GAS))+'장','s','무엇을 뿜나','미생물이 만들어내는 가스 — 냄새·독성을 지닌 것과 무취 부산물.',GAS)+'</div></section>\n\n'
'<section><div class="wrap">\n'+sec('⑤ 회로 · '+str(len(MECH))+'장','','어떻게 몸을 흔드나','가스와 세균이 실제로 몸을 무너뜨리는 통로 — 기전 카드.',MECH)+'</div></section>\n\n'
'<section class="alt"><div class="wrap">\n'+sec('⑥ 결과 · '+str(len(SX))+'장','','무엇으로 드러나나','상류가 흔들면 하류에 나타나는 증상들 — 각 카드는 원인 카드를 거꾸로 가리킵니다.',SX)+'</div></section>\n\n'
'<section><div class="wrap">\n'+sec('⑦ 반대편 · '+str(len(FIX))+'장','','어떻게 벗어나나','나쁜 카드의 짝 — 측정하고, 굶기고, 다스리는 도구와 해법.',FIX)+'</div></section>\n\n'
'<section class="alt"><div class="wrap">\n'+sec('⑧ 무기 · '+str(len(DRUG))+'장','','무엇으로 다스리나','제균에 쓰는 항생제와 항진균제. 어떤 약이 어떤 표적을 겨누는지 — 실제 처방·용량은 반드시 진료로.',DRUG)+'</div></section>\n'
)

CARDCSS='''
  :root{--mech:#5860c8;--fix:#2f9160;--drug:#3f7f97;--sx:#a8465f}
  @media(prefers-color-scheme:dark){:root{--mech:#93a0f2;--fix:#5cc78c;--drug:#74b8d0;--sx:#e492a6}}
  :root[data-theme="dark"]{--mech:#93a0f2;--fix:#5cc78c;--drug:#74b8d0;--sx:#e492a6}
  :root[data-theme="light"]{--mech:#5860c8;--fix:#2f9160;--drug:#3f7f97;--sx:#a8465f}
  .deck{display:grid;grid-template-columns:repeat(auto-fill,minmax(186px,1fr));gap:16px;margin-top:22px}
  .pcard{position:relative;display:flex;flex-direction:column;background:var(--surface);border:1px solid var(--line);
    border-radius:16px;padding:20px 18px 16px;overflow:hidden;--c:var(--accent);
    transition:transform .15s ease,box-shadow .15s ease,border-color .15s ease}
  .pcard::before{content:"";position:absolute;left:0;right:0;top:0;height:3px;background:var(--c);z-index:2}
  .pcard:hover{transform:translateY(-4px);border-color:var(--c);box-shadow:0 18px 36px -22px #0008}
  .pcard.gas{--c:var(--sulfur-line)} .pcard.sub{--c:var(--danger)} .pcard.mech{--c:var(--mech)}
  .pcard.fix{--c:var(--fix)} .pcard.drug{--c:var(--drug)} .pcard.sx{--c:var(--sx)}
  .pglyph{height:92px;display:grid;place-items:center;color:var(--c);margin-bottom:12px}
  .pglyph svg{width:82px;height:82px}
  /* 사진 아트: 카드 상단 배너로 꽉 채움 (padding 상쇄 후 가장자리까지 bleed) */
  .pglyph.img{height:132px;display:block;margin:-20px -18px 14px;background:var(--surface2)}
  .pglyph.img img{width:100%;height:100%;object-fit:cover;display:block}
  .psci{font-family:var(--mono);font-size:10px;letter-spacing:.03em;color:var(--faint);line-height:1.3;min-height:26px}
  .pname{font-size:19px;font-weight:800;letter-spacing:-.02em;margin:3px 0 9px;line-height:1.15}
  .pbadge{align-self:flex-start;font-family:var(--mono);font-size:9.5px;font-weight:600;letter-spacing:.08em;
    text-transform:uppercase;padding:3px 8px;border-radius:5px;background:color-mix(in srgb,var(--c) 15%,transparent);color:var(--c);margin-bottom:11px}
  .pdesc{font-size:12.8px;color:var(--ink2);line-height:1.55;flex:1}
  .pmeta{margin-top:11px;font-family:var(--mono);font-size:10.5px;color:var(--c);border-top:1px solid var(--line);padding-top:9px;line-height:1.5}
  .pmeta s{color:var(--faint)}
  .deckhero{padding:30px 0 8px;border-bottom:1px solid var(--line)}
'''

HTML=('<!doctype html>\n<html lang="ko">\n<head>\n<meta charset="utf-8">\n'
'<meta name="viewport" content="width=device-width, initial-scale=1">\n'
'<title>개념 카드덱 — '+T+'장으로 보는 균·가스·먹이·기전·증상·약 | Neo-Skepticism</title>\n'
'<meta name="description" content="SIBO·SRB·후소박테리움·GLP-1·호흡가스 분석기·항생제·대장암까지 — 만성 증상 뒤의 무대·먹이·용의자·산물·회로·결과·반대편·무기를 '+T+'장의 카드로. 양준상 MD Neo-Skepticism (교육 목적).">\n'
'<link rel="stylesheet" href="style.css">\n<style>'+CARDCSS+'</style>\n</head>\n<body>\n'
'<nav><div class="wrap row">\n  <a class="brand" href="index.html"><span class="dot"></span>Neo-Skepticism <small>양준상 MD</small></a>\n'
'  <div class="navlinks">\n    <a href="index.html">홈</a>\n    <a href="index.html#assess">자가진단</a>\n    <a href="index.html#mechanism">기전</a>\n'
'    <button class="theme" id="themeBtn" aria-label="테마 전환">◐</button>\n  </div>\n</div></nav>\n\n'
'<div class="wrap"><div class="crumb"><a href="index.html">Neo-Skepticism</a> · <span>개념 카드덱</span></div></div>\n\n'
'<header class="hero deckhero"><div class="wrap">\n  <span class="eyebrow s">'+T+' CARDS · 개념 카드덱</span>\n'
'  <h1>흩어진 이름들을, 한 벌의 카드로.</h1>\n'
'  <p class="lede">SIBO·SRB·후소박테리움·메틸메르캅탄·GLP-1·호흡가스 분석기·항생제… 진료에서 자주 나오는 이름들을 <b>무대 · 먹이 · 용의자 · 산물 · 회로 · 결과 · 반대편 · 무기</b> 여덟 갈래로 정리했습니다. 각 카드가 무엇을 만들고 어디로 이어지는지 한눈에.</p>\n'
'</div></header>\n\n'
+BODY+
'\n<section><div class="wrap narrow">\n  <div class="consult"><h2>이 카드들이 당신 안에서 어떻게 엮이는지.</h2>'
'<p>증상 자가진단으로 당신의 패턴이 어느 카드와 맞는지 확인하고, 필요하면 상담으로 이어가세요.</p>\n'
'  <a href="index.html#assess" class="btn" style="background:#fff;color:var(--accent2)">자가진단 하러 가기 →</a></div>\n'
'  <p class="disc"><b>고지.</b> 각 카드는 양준상 MD의 임상 프레임을 <b>교육·성찰 목적</b>으로 요약한 것으로, 특정 질병의 진단·치료·처방을 뜻하지 않습니다. 결과·증상 카드는 원인과의 <b>연결이 연구·지목된다</b>는 뜻이지 인과의 단정이 아니며, 항생제·항진균제 카드는 약의 성격을 소개할 뿐 처방·용량 안내가 아닙니다. 실제 진단·치료는 반드시 의사의 진료로 결정하세요.</p>\n'
'</div></section>\n\n'
'<footer><div class="wrap">\n  <a class="brand" href="index.html" style="margin-bottom:16px"><span class="dot"></span>Neo-Skepticism <small>양준상 MD</small></a>\n'
'  <div class="dl"><b>고지.</b> 교육·성찰 목적의 콘텐츠이며 의학적 조언을 대체하지 않습니다.</div>\n'
'  <div style="margin-top:18px;font-family:var(--mono);font-size:11.5px">© 2026 Neo-Skepticism · 양준상 MD</div>\n</div></footer>\n\n'
'<script>\n(function(){var root=document.documentElement;'
'document.getElementById("themeBtn").addEventListener("click",function(){var c=root.getAttribute("data-theme");'
'if(!c){c=matchMedia("(prefers-color-scheme:dark)").matches?"dark":"light";}root.setAttribute("data-theme",c==="dark"?"light":"dark");});})();\n</script>\n'
'</body>\n</html>\n')

open('card.html','w',encoding='utf-8').write(HTML)
miss=[r[2] for grp in groups for r in grp if r[2] not in G]
print('card.html', len(HTML), 'bytes ·', HTML.count('class="pcard'), 'cards · total', total, '· missing glyphs:', miss or 'none')
