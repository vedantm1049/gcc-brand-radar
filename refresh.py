"""Weekly refresh. Usage: python3 refresh.py scraped.json YYYY-MM-DD
scraped.json: list of {"username":..., "followersCount":..., "postsCount":...} from apify/instagram-profile-scraper.
Appends a snapshot to history.json (skips if that date already exists) and rebuilds index.html."""
import json,sys,datetime,subprocess
rows=json.load(open(sys.argv[1])); day=sys.argv[2]
d=datetime.date.fromisoformat(day); label=f"{d.day} {d.strftime('%b')}"
handles=set(json.load(open('handles.json')))
f={r['username']:r['followersCount'] for r in rows if r.get('username') in handles and r.get('followersCount')}
p={r['username']:r.get('postsCount') for r in rows if r.get('username') in handles}
H=json.load(open('history.json'))
if any(s['date']==day for s in H): sys.exit(f'snapshot {day} already exists')
if len(f)<len(handles)*0.6: sys.exit(f'only {len(f)} of {len(handles)} profiles returned; not saving')
H.append(dict(date=day,label=label,f=f,p=p)); json.dump(H,open('history.json','w'),indent=1)
subprocess.run(['python3','build2.py'],check=True)
print('saved',label,len(f),'profiles')
