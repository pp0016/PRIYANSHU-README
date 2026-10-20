import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def create_dossier():
    doc = docx.Document()

    # Margins
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # Document Header
    p_title = doc.add_paragraph()
    r_title = p_title.add_run("QUIET MONEY POV (@quietmoneypov)")
    r_title.font.name = "Arial"
    r_title.font.size = Pt(22)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(17, 24, 39)
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    p_sub = doc.add_paragraph()
    r_sub = p_sub.add_run("Top 7 Viral Launch Sequence & Deep Packaging Blueprints\nComprehensive vidIQ Algorithm & Outlier Forensics Dossier")
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(12)
    r_sub.font.italic = True
    r_sub.font.color.rgb = RGBColor(75, 85, 99)
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # 1. Executive Summary & Strategic Findings
    p_h1 = doc.add_heading(level=1)
    r_h1 = p_h1.add_run("1. Executive Summary & Algorithm Findings")
    r_h1.font.name = "Arial"
    r_h1.font.bold = True
    r_h1.font.color.rgb = RGBColor(30, 58, 138)

    findings = [
        ("The Institutional Explainer Ceiling:", " A brand-new 3,320-sub channel produced a 637K view video at 4,351.8x its channel average with competition of just 18 (Luxury Hotels). This unlocked an ultra-high-ceiling category with low saturation."),
        ("Wealth Ladder Upgrade ($10M -> $25M):", " The live 1.14M-view benchmark uses $25M with 78,708 monthly searches on the exact phrase. Episode 1 was upgraded accordingly to capture existing search and suggested traffic."),
        ("Dead Keywords Purged:", " Confirmed zero-volume/blocked keywords (homeownership myth, high income poor, middle class trap with 66.7% India volume) were purged and rerouted into high-US-volume assets (Renting vs Buying: 1.7M proof)."),
        ("The Strategic Sequence Logic:", " Ep 1 buys cold reach (ladder), Ep 2 buys identity/loyalty (score 98), Ep 3 proves the ceiling (4,351x breakout), Ep 4 triggers financial consequence, Ep 5 breaks rhythm with mechanics, Ep 6 drives high-arousal comments, and Ep 7 banks permanent evergreen search traffic.")
    ]

    for title, desc in findings:
        p = doc.add_paragraph(style='List Bullet')
        r1 = p.add_run(title)
        r1.font.name = "Arial"
        r1.font.bold = True
        r2 = p.add_run(desc)
        r2.font.name = "Arial"

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # 2. Table of Top 7
    p_h2 = doc.add_heading(level=1)
    r_h2 = p_h2.add_run("2. The Locked Top 7 Launch Sequence")
    r_h2.font.name = "Arial"
    r_h2.font.bold = True
    r_h2.font.color.rgb = RGBColor(30, 58, 138)

    table = doc.add_table(rows=1, cols=6)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr_cells = table.rows[0].cells
    headers = ["Ep #", "Production Title", "Score", "Origin", "Target Keyword", "Comp"]
    for i, h in enumerate(headers):
        hdr_cells[i].text = h
        hdr_cells[i].paragraphs[0].runs[0].font.bold = True
        hdr_cells[i].paragraphs[0].runs[0].font.name = "Arial"
        hdr_cells[i].paragraphs[0].runs[0].font.size = Pt(9.5)
        hdr_cells[i].paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
        shading = parse_xml(r'<w:shd {} w:fill="1E3A8A"/>'.format(nsdecls('w')))
        hdr_cells[i]._tc.get_or_add_tcPr().append(shading)

    rows_data = [
        ("1", "How Banks Treat You at Every Level of Wealth ($0 to $25M)", "92", "Candidate #2 (Upgraded)", "how banks treat you at every level of wealth", "53.4 (1.14M Proof)"),
        ("2", "Why You Must Look Like a Loser to Escape the Rat Race", "98", "EXTERNAL FIND (Gold)", "quiet wealth", "32.4 (831K Proof)"),
        ("3", "How Luxury Hotels Make Money From Rooms Nobody Sleeps In", "90 / 97", "EXTERNAL FIND (Ceiling)", "how luxury hotels make money", "18.0 (4,351x Breakout)"),
        ("4", "POV: Your $650 Car Payment Built Someone Else's $793,000", "95", "Candidate #10 (Upgraded)", "car loan mistakes", "30.2 (304K Proof)"),
        ("5", "How Pawn Shops Actually Make Money (They Hope You Never Return)", "93", "Candidate #7 (Upgraded)", "how pawn shops actually make money", "26.3 (+2,185% Surge)"),
        ("6", "Why Your Family Treats You Differently When You Become First Millionaire", "97", "Candidate #9 (Upgraded)", "income vs wealth", "29.8 (High Comments)"),
        ("7", "Renting vs Buying a Home: The 20-Year Math That Decides It", "96", "EXTERNAL FIND (Search)", "renting vs buying", "57.5 (1.7M Proof)")
    ]

    for r in rows_data:
        row_cells = table.add_row().cells
        for i, val in enumerate(r):
            row_cells[i].text = val
            p = row_cells[i].paragraphs[0]
            if p.runs:
                p.runs[0].font.name = "Arial"
                p.runs[0].font.size = Pt(9)

    doc.add_page_break()

    # 3. Deep Packaging Blueprints
    p_h3 = doc.add_heading(level=1)
    r_h3 = p_h3.add_run("3. Forensic Packaging Blueprints (Episodes 1 to 7)")
    r_h3.font.name = "Arial"
    r_h3.font.bold = True
    r_h3.font.color.rgb = RGBColor(30, 58, 138)

    blueprints = [
        {
            "ep": "EPISODE 1: How Banks Treat You at Every Level of Wealth (From $0 to $25M)",
            "score": "92 (Parenthesis version) | Alternatives: Banks Treat You Differently at Every Level of Wealth — $0 to $25M (88) | How Banks Treat You at Every Level of Wealth — $0, $100K, $1M, $25M (91)",
            "origin": "Candidate #2, upgraded from $10M to $25M per live research.",
            "metrics": "how banks treat you at every level of wealth (78,708 searches, comp 53.4) paired with wealth ladder (15,444, comp 31) and quiet wealth (148,726, comp 32.4).",
            "benchmark": "Dark Ledger (1,146,600 views, 238.2x breakout) | Finance POV (420,990 views on 25.4k subs) | Banks Don't Want You Knowing About the $25K Rule (107,016 views, 128.5x on 3.5k subs).",
            "thumbnail": "Foreground: Plain bank lobby counter. Left: Stoic stickman in worn jacket, hands at sides, single overdraft notice on counter. Right: Banker in crisp suit, eyebrows raised, mouth slightly open in shocked disbelief ('you're that tier' face). Diegetic UI: ATM screen behind them reading $25,000.00 (the tier threshold). Background: Warm suburban bank branch, afternoon light, no void black. Bottom-right 180x40px clear.",
            "hook": "0.8s rapid cuts: Overdraft notice, $35 fee, private-client luxury room. Spoken: \"There's a line in banking. Below it, you pay the fees. Above it, the bank competes for you.\" Stickman stands on the wrong side.",
            "gap": "Competitors stop at fee lists. Our gap: Name the exact psychological and behavioral tier classification line, prove the tier is reachable, and affirm viewer reality with permission rather than preachy advice.",
            "math": "Overdraft fee = $35 (FDIC baseline). Median US household income $87,460 = $42/hr; one fee = 50 min of gross labor. Compound rate pinned strictly to 6.69% real S&P 500 historical average."
        },
        {
            "ep": "EPISODE 2: Why You Must Look Like a Loser to Escape the Rat Race",
            "score": "98 (HIGHEST SCORE OF ENTIRE PASS) | Alternatives: POV: You Looked Broke While Everyone Else Looked Successful | 7 Stealth Wealth Habits That Make You Look Poor on Purpose",
            "origin": "⭐ EXTERNAL DISCOVERY — not on original list. The ultimate identity/loyalty handshake.",
            "metrics": "quiet wealth (148,726 searches, comp 32.4) | stealth wealth habits (5,123, comp 28.7) | why rich people look poor (5,284, comp 40.5 in description). Avoid high-comp tags like stealth wealth (49).",
            "benchmark": "Why You Must Look Like a Loser (831,174 views, 2,222.7x breakout on 4,770-sub channel, 148 VPH) | Why Real Wealth Looks Boring (183,262 views, 131x on 6.6k subs).",
            "thumbnail": "Split-frame dinner table. Left: Stoic stickman in plain shirt, wallet closed, completely neutral. Right: Coworker holding heavy metal card toward camera, mouth open mid-boast, eyebrows high. Object contrast: Dented hatchback keyring vs luxury brand crest fob. Diegetic UI: Coworker phone showing $4,200 balance alert. Warm restaurant, evening light. Bottom-right clear.",
            "hook": "1.2s cuts: Split dinner bill, heavy metal card slammed down, stickman pays exact cash. Voice: \"The people pitying you are the ones falling behind.\" Cut to him driving dented car, then cut to his quiet brokerage balance.",
            "gap": "Generic videos glorify frugality. We address the unspoken social tax: the awkwardness, family comments, and pity from broke peers, giving viewers permission to look poor on purpose.",
            "math": "$765/mo car payment invested at 6.69% real for 30 years = $878,000. Unit conversion: Each $10,000 of lifestyle inflation = $238/day of future freedom destroyed at 30 years."
        },
        {
            "ep": "EPISODE 3: How Luxury Hotels Make Money From Rooms Nobody Sleeps In",
            "score": "90 (Production) / 97 (POV version: POV: You Booked a $400 Hotel Room — Here's What It Really Cost) | Alt: How Luxury Hotels Make Money From Empty Rooms (91)",
            "origin": "⭐ EXTERNAL DISCOVERY — Highest single breakout ceiling found (4,351x on 3,320 subs).",
            "metrics": "how luxury hotels make money (9,287 searches, comp 18.0 — lowest competition in entire niche!) | how hotels make money (17,036, comp 30.5) | finance explained (514k, comp 24.2).",
            "benchmark": "How Luxury Hotels Make Money From Empty Rooms (637,012 views, 4,351.8x breakout on 3,320 subs, 164 VPH, published 26 days ago) | Cruise Lines Trap You at Every Level (160,909 views, 292.9x on 1,130 subs).",
            "thumbnail": "Foreground: Hotel corridor with closed doors and 'SOLD OUT' folio on desk vs brass room-key tray. Stoic stickman stands at reception in plain travel clothes. Front-desk clerk leans in with a knowing half-smile and raised brows. Diegetic UI: Reception monitor angled to camera reading 94% OCCUPANCY — 0 ROOMS. Warm marble lobby. Bottom-right clear.",
            "hook": "0.8s cuts: Closed door, sold out sign, group contract page, same room photographed twice in one night. Voice: \"In 2020 the Ritz London closed all 136 rooms. The same week, someone paid 800 million pounds for the building. That only makes sense once you know what a luxury hotel actually sells.\"",
            "gap": "Textbooks explain RevPAR and occupancy. We expose the hostile mechanics: Non-refundable rates allowing a single room to be sold twice in one night, and corporate attrition clauses billing companies for unused beds.",
            "math": "Double-billing margin model + 200-room block at 70% pickup clause = 60 unsold rooms billed at full price with zero housekeeping cost. Margin-based mechanics cited from real hotel contracts."
        },
        {
            "ep": "EPISODE 4: POV: Your $650 Car Payment Built Someone Else's $793,000",
            "score": "95 (Specific dollar version outscores generic 86 by 9 points) | Alts: POV: You Quietly Stopped Paying Car Payments — Everything Changed (86) | Buying vs Leasing a Car: The Math Nobody Shows You",
            "origin": "Candidate #10 rebuilt around verified external outlier proof (304K views on 1,810 subs).",
            "metrics": "car loan mistakes (3,977, comp 30.2) | car debt (comp 50.5 in tags) | car payments trap (comp 43.3) | average car payment (comp 51.1).",
            "benchmark": "Buying vs Leasing a Car: The Math Nobody Shows You (304,805 views, 856.1x breakout on 1,810 subs, 168.9 VPH) | How Car Washes Make Money (182,040 views, 20x on 2.5k subs).",
            "thumbnail": "Driveway scene. Left: Dented older sedan with stoic stickman leaning against it, arms crossed, neutral. Right: Brand-new financed truck with paper temporary plate, neighbor standing beside it with chin lifted in smug pride. Diegetic UI: Neighbor phone held at hip reading $765/MO — 72 MONTHS. Golden hour suburban street. Bottom-right clear.",
            "hook": "0.9s cuts: Signing contract, handing over keys, paper plate flapping, $765 leaving bank account. Voice: \"The average American new-car payment is $765 a month. Nobody notices it leaving. Everybody notices it arrived.\"",
            "gap": "Competitors compare sticker MSRP. We expose the dealer's back-end: Dealer reserve kickbacks from lenders and payment-packing tactics that sneak warranties into monthly figures.",
            "math": "Average new vehicle loan: $765/mo (LendingTree/NerdWallet/Experian 2026). S&P 500 model: $765/mo at 6.25% real for 30 years = $793,000 (at 6.69% real = $878,000). Both strictly verified."
        },
        {
            "ep": "EPISODE 5: How Pawn Shops Actually Make Money (They Hope You Never Return)",
            "score": "93 | Alts: How Pawn Shops Actually Make Money (84) | The Pawn Shop Model: They Profit When You Don't Come Back",
            "origin": "Candidate #7 strengthened — verified as the single highest growth keyword in the entire niche (+2,185%).",
            "metrics": "how pawn shops actually make money (87,373 searches, comp 26.3, US 17,475, +2,185.46% surge).",
            "benchmark": "How to Make Banks Work for You (447,796 views, 243.5x breakout, 554 VPH on 8k subs) | Building a Holding Company (226,276 views, 108.4x on 12.5k subs).",
            "thumbnail": "Pawn shop counter. Stoic stickman slides wedding ring across; receives thin cash stack and paper ticket. Pawnbroker holds ticket with knowing smirk and raised brow. Object contrast: Back wall shelf of unclaimed guitars, watches, laptops. Diegetic UI: Pawnbroker tablet angled to camera showing 30 DAYS — 240% APR. Strip-mall neon daylight. Bottom-right clear.",
            "hook": "1.0s cuts: Ring on scale, ticket torn, shelf of abandoned belongings. Voice: \"You borrow $180 against a $600 ring. It takes four minutes. It takes you seven months to get it back — if you ever do.\" What happens on day 31.",
            "gap": "Competitors show inventory flips. We explain the emotional predator model: Pawn shops are the only lenders with zero credit checks, pricing loans for people with no other door.",
            "math": "APRs run 60%-240% (Amerisave / Texas OCCC bracket regulations). Average loan: $180. Unit conversion: 240% APR on $180 = 1 hour of median labor ($42) every 26 days just to rent your own ring."
        },
        {
            "ep": "EPISODE 6: Why Your Family Treats You Differently When You Become the First Millionaire",
            "score": "97 (Highest emotional arousal score) | Alts: POV: Your Family Found Out You're the First Millionaire — Things Got Weird | What Every Level of Wealth Actually Feels Like",
            "origin": "Candidate #9 upgraded from generic wealth into the high-comment family friction angle.",
            "metrics": "income vs wealth (4,267, comp 29.8) | quiet wealth (comp 32.4) | how your family treats you at every level (14,570 searches, comp 26.0).",
            "benchmark": "How Banks Treat You (420,990 views on 25.4k subs) | Your Life at Every Salary Level (299,733 views, 62.3x) | Seniors 65+ 5 Bills (790,443 views, 118x on 12k subs).",
            "thumbnail": "Family dining table, Sunday lunch. Stoic stickman sits with plain glass of water, neutral. Relative leans across table with wide begging eyes and open mouth ('so can you help me?'); second relative has arms folded, jaw clenched in jealous side-eye. Diegetic UI: Stickman phone face-down vs relative phone showing balance alert. Warm suburban dining room. Bottom-right clear.",
            "hook": "1.1s cuts: Family group chat ping, cousin asking for 'a small favor', cousin's strained face at dinner table, stickman flipping phone face-down. Voice: \"When you become the first person in your family to have money, you don't get applause. You get a new job.\"",
            "gap": "Every video teaches how to get money. None cover what happens to family dynamics after: Loan demands, quiet resentment, shifting tone, and guilt-tripping.",
            "math": "$1,000,000 at 6.69% real produces $66,900/year real return = $5,575/month. Reframe: A relative asking for $10,000 is asking for 1.8 months of everything your life savings generates."
        },
        {
            "ep": "EPISODE 7: Renting vs Buying a Home: The 20-Year Math That Decides It",
            "score": "96 (Permanent search and suggested browse engine) | Alts: How Are Americans Affording $600,000 Homes on Average Salaries? (84) | Renting vs Buying a Home — Who Actually Builds More Wealth in 20 Years?",
            "origin": "⭐ EXTERNAL DISCOVERY — Replaced blocked Candidate #20. Backed by 1.7M-view verified proof.",
            "metrics": "renting vs buying (74,297 searches, comp 57.5) paired with income vs wealth (comp 29.8) and finance explained (comp 24.2).",
            "benchmark": "Renting Vs Buying - The Real Math (1,703,597 views, 246.2x breakout, 948 VPH on 25.8k subs) | How Are Americans Affording $600k Homes (501,591 views, 62.3x on 7.9k subs).",
            "thumbnail": "Two identical suburban houses side by side. Left driveway: Stoic stickman holding keys and mortgage letter, neutral. Right driveway: Neighbor holding same keys with furrowed brow, distressed mouth, hunched shoulders. Object contrast: Moving box on porch vs neighbor expensive landscaping and financed second car. Diegetic UI: Neighbor phone showing 7.40% — $4,100/MO. Bottom-right clear.",
            "hook": "1.2s cuts: Two signatures on two identical deeds, two sets of keys, two statements differing by hundreds. Voice: \"Two people bought the same house on the same street, same week. Twenty years later, one of them is ahead by a figure nobody puts in a headline.\"",
            "gap": "Every video picks a side early and preaches. We reveal the exact mathematical crossover point where renting beats buying (and vice-versa) based on real mortgage interest amortization vs compounding equity.",
            "math": "30-year fixed at 7.40% (national baseline). On a $555,000 home, principal + interest = $1,383,000 (total interest alone = $828,000!). Compares down payment delta invested at 6.69% real, mapping exact crossover year."
        }
    ]

    for b in blueprints:
        p_ep = doc.add_heading(level=2)
        r_ep = p_ep.add_run(b['ep'])
        r_ep.font.name = "Arial"
        r_ep.font.bold = True
        r_ep.font.color.rgb = RGBColor(30, 58, 138)

        sections = [
            ("1. Title & Scores:", b['score']),
            ("2. Origin / Source:", b['origin']),
            ("3. Target Keywords & Metrics:", b['metrics']),
            ("4. Verified Outlier Benchmarks:", b['benchmark']),
            ("5. High-CTR Thumbnail Concept (8 Laws):", b['thumbnail']),
            ("6. First 45-Second Hyper-Hook:", b['hook']),
            ("7. The 40% Knowledge & Emotional Gap:", b['gap']),
            ("8. Verified Real-Rate Math Model:", b['math'])
        ]

        for label, text in sections:
            p = doc.add_paragraph()
            r1 = p.add_run(label + " ")
            r1.font.name = "Arial"
            r1.font.bold = True
            r1.font.size = Pt(10)
            r2 = p.add_run(text)
            r2.font.name = "Arial"
            r2.font.size = Pt(10)

        doc.add_paragraph().paragraph_format.space_after = Pt(10)

    out_path = r"c:\Users\renu5\Downloads\priyanshu readme\youtube\Stickman\finance Stickman\TOP_7_LAUNCH_RESEARCH_AND_PACKAGING_DOSSIER.docx"
    doc.save(out_path)
    print(f"File created successfully: {out_path}")

if __name__ == "__main__":
    create_dossier()
