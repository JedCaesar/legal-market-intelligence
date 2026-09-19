from __future__ import annotations
import csv
from collections import Counter, defaultdict
from dataclasses import dataclass

@dataclass(frozen=True)
class Case:
    city:str; case_type:str; revenue:float; local_lawyers:int

@dataclass(frozen=True)
class MarketScore:
    city:str; case_count:int; revenue:float; top_case_type:str; local_lawyers:int; opportunity_score:float

def load_cases(path="cases.csv"):
    with open(path,newline="",encoding="utf-8") as f:
        return [Case(r["city"],r["case_type"],float(r["revenue"]),int(r["local_lawyers"])) for r in csv.DictReader(f)]

def analyze_markets(cases):
    if not cases: return []
    grouped=defaultdict(list)
    for case in cases: grouped[case.city].append(case)
    max_cases=max(map(len,grouped.values()))
    max_revenue=max(sum(c.revenue for c in items) for items in grouped.values())
    max_lawyers=max(items[0].local_lawyers for items in grouped.values())
    scores=[]
    for city,items in grouped.items():
        revenue=sum(c.revenue for c in items); lawyers=items[0].local_lawyers
        score=100*(.4*len(items)/max_cases+.4*revenue/max_revenue+.2*(1-lawyers/max_lawyers))
        top=Counter(c.case_type for c in items).most_common(1)[0][0]
        scores.append(MarketScore(city,len(items),revenue,top,lawyers,round(score,1)))
    return sorted(scores,key=lambda x:x.opportunity_score,reverse=True)

def report(scores):
    lines=["# Legal Market Opportunity Report","","| Rank | City | Cases | Revenue | Top demand | Local lawyers | Score |","|---:|---|---:|---:|---|---:|---:|"]
    for rank,x in enumerate(scores,1):
        lines.append(f"| {rank} | {x.city} | {x.case_count} | USD {x.revenue:,.0f} | {x.top_case_type} | {x.local_lawyers} | {x.opportunity_score} |")
    return "\n".join(lines)

if __name__=="__main__": print(report(analyze_markets(load_cases())))
