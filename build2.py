"""Build index.html from template2.html + data files. Usage: python3 build2.py"""
import json
D=json.load(open('radar.json')); H=json.load(open('history.json'))
C=json.load(open('copy.json')); M=json.load(open('memos.json'))
P={
"Zaphira Nature":("Saudi launch in Oct 2026 and Kuwait via Curlnation, on top of a UAE salon network that stocks the range with no upfront cost.","0.65% median engagement on 5.3K followers, plus 4 verified retail and salon partners across 3 markets.","Small audience. Salon distribution builds trust but scales slowly. Curly and textured hair is a focused niche."),
"MZN Bodycare":("Distribution is already built: 80+ retail partners, Faces and pharmacy chains. Social is the weak link, which is where a creator-led owner adds most.","42.5K followers but 0.01% median engagement (about 6 interactions per post).","Founded 2015, so not a young brand. Handmade production may cap volume. Value positioning."),
"Nutrili":("Just moved from online-only to shelves (Spinneys) and sells on Ounass in 3 markets.","20,000+ customers and shipping to 15 countries, from a 2022 start.","Supplement rules differ by market. A second brand can split focus. Engagement not measured."),
"Passion Labs":("A chemist-founder, Arabic-first brand with a real community around natural skin, hair and soap.","0.54% median engagement on 21.9K followers.","Only one verified retailer. Little public information on the founder or the business."),
"Gaudia Beauty":("Launched a travel-size Mini Set in Oct 2026, in the fastest-growing category in the region.","Highest momentum score on the list: 0.8% median engagement and about 9 posts a month.","No verified retail. 2.9K followers, so very early."),
"AÏZA (Amaani)":("Benchmark, not a target: Ulta ME top-10 brand within a year, net revenue up 9x+ year on year in H1 2026.","$8M raised; Series A led by BECO in Sep 2026.","Already priced by specialist funds. HBI would be a follower, not a lead."),
"3 of Cups":("Watchlist. One hero product with a clear hook (a face mask you use in the shower).","3.2% median engagement, but on only 585 followers.","Too early to judge. One product."),
"Shake Your Plants":("On shelves through the Spinneys incubator and Powder Beauty, with a Shark Tank deal behind it.","AED 1.2M for 20% from Amira Sajwani (Jun 2025), implying about AED 6M post-money.","Overlaps Humantra on hydration. Could be a bolt-on or a conflict: an HBI call."),
}
last=H[-1]['f']
for b in D['B']:
    h=b.get('handle')
    if h and h in last: b['fol']=last[h]
data=dict(B=D['B'],C=D['C'],P=P,W=C['W'],T=C['T'],M=M,H=H)
t=open('template2.html').read().replace('/*DATA*/',json.dumps(data,ensure_ascii=False))
open('index.html','w').write(t); print('built',len(t),'snapshots',len(H))
