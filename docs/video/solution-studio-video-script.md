# Mastercard Solution Studio — walkthrough video script

5 min 23 s · 1920×1080, 30 fps · voice: Kokoro-82M v1.0 (`af_heart`), one sentence at a time with explicit pauses · made by `tools/video/` (see its README)

**Watch the latest cut: [Mastercard-Solution-Studio.mp4](Mastercard-Solution-Studio.mp4)** (5 min 23 s). This take was recorded where Mastercard's logo host can't be reached, so the merchant logos are stand-ins of the same brands (see below); a render that can reach it shows the API's own.

The narration below is the source of truth in [`tools/video/narration.json`](../../tools/video/narration.json); edit it there and re-run the pipeline. Timings are from the current voice track. *Italic brackets* are what happens on screen.

---

## 0:01 · Mastercard's mission (18 s)

At Mastercard, our mission is to power economies and empower people. Every day, that means connecting billions of people, millions of businesses and thousands of banks, safely and simply, all around the world.

So how do you build on all of that? That's where Mastercard Solution Studio comes in.

*[Home: the Solution Studio title, the revolving dot globe and the cards cycling through use cases, APIs and bundles. No cursor.]*

## 0:19 · Platform for the world's economies (51 s)

Solution Studio helps you navigate, and innovate, across everything Mastercard has to offer.

We've mapped all of it as one platform for the world's economies: five layers, from the network at its core, up to the ways you plug in. Because there's a lot more to Mastercard than a card network.

There are the rails behind entire national payment systems, moving money between bank accounts in real time. Tokens that keep card numbers out of phones, wallets and websites, and AI that scores every transaction in milliseconds. Cyber intelligence that spots stolen cards before they're used. Open finance, so people can share their bank data, with consent, and get a loan decision in minutes. Insights from the spending that flows across the network, loyalty, and Priceless experiences. And now, agentic commerce, where AI agents can shop and pay for you, safely.

*[The cursor opens the "Platform for the world's economies" tab. The page changes around the globe, which stays exactly where it was on Home. On "one platform for the world's economies" it moves into the picture and is cut into five slices that settle into the stack; the heading, now "Mastercard Platform for the world's economies", and the list of layers fade in. The stack opens out, and each example is pointed at on its layer as it is named: Rails and its A2A & real-time area; Network services, Tokenisation & credentials then Risk decisioning; Solutions, Security Solutions; Rails again, Open Finance; Solutions, Insights & Intelligence then Consumer Acquisition & Engagement; Network services, Agentic commerce.]*

## 1:10 · Use cases through the layers (65 s)

Choose who you are and what you want to solve, and the areas that deliver it light up across the layers, in the order they act. For a bank cutting fraud, that's threat intelligence, tokens, authentication, and a risk score on every payment.

Now take something bigger: a government getting money to people, quickly and safely. Payments go out on Bacs, which runs on Mastercard's Vocalink, and already pays more than 95% of UK salaries. Mastercard Move pays out to cards, bank accounts and wallets, and Send can push funds to a card in seconds. Where people have no bank account, Community Pass gives them a digital identity, so the money still reaches them. A2A Protect screens every payment for scams before it leaves. And SpendingPulse shows how that money then moves through the economy. Rails, security, insights and inclusion, working together as one platform.

Each area lists its products, and the orange markers show what you can try live, right here in Studio. Let's take BIN Lookup, which tells you all about a Mastercard card range. Every API is just one click away.

*[The cursor picks the solution "Cut fraud without declining good customers": the circuit lights from the bank down through Solutions, Network services and into the Kernel, numbered in order, and each step is pointed at as it is named. Then "Who" → "A government" → "Get payments to people quickly and safely": a new circuit runs from the government through Rails (Bacs; Mastercard Move and Send), the inclusion pillar (Community Pass) and Solutions (A2A Protect, SpendingPulse), and each of the six steps is pointed at as it is named; the cursor ends over the lit stack. The Kernel layer comes forward with its areas and orange markers; Franchise & rules opens, the BIN Lookup card expands to "Try it in Solution Studio", and the cursor clicks the BIN Lookup API button.]*

## 2:15 · A live API (12 s)

Each API comes pre-wired, with authentication and request signing handled for you. Pick a card range, hit send, and there's the response. The issuer, the product, the country, in about a second.

*[The APIs tab opens on BIN Lookup. The cursor picks "Lookup BIN" and clicks Send; the request and a 200 response appear.]*

## 2:27 · API bundles (22 s)

APIs are even more powerful together, so we've grouped them into bundles built around real business problems. Merchant Resolution, for example, combines Consumer Clarity, Merchant Identifier and Places. So cardholders always recognise who they paid, and fewer disputes ever start.

Every bundle walks you through how the APIs fit together, step by step.

*[The API Bundles tab opens on Merchant resolution: header, hero visual, what you can do. The page scrolls to "How the APIs fit together" and the walkthroughs.]*

## 2:49 · Data enrichment (17 s)

Then there are use cases: complete experiences that bring the APIs to life.

Let's start simple. This is what a bank statement really looks like. And this is the same data after Mastercard enriches it. The real merchant, its logo, a proper category, and where to find it.

*[Use Cases → Data Enrichment. Raw statement lines such as `SBUX 00654321 CARD 12345` and `AMZN MKTP US*MK7G3B2X1` sit with "Merchant unknown". The cursor enriches the first one, then "Enrich all": each becomes the merchant's name and logo, its category, its website and, where the data has one, its location.]*

## 3:06 · Find A Card (53 s)

Find A Card goes further. It shows how an AI agent could find the right card for you.

You start by telling the agent what you want, in your own words. Then, with your permission, it connects to your bank through Open Finance, and learns how you really spend. Where the money goes, how often you travel, and how much you spend abroad.

From that, it builds its own search, and scores every card on value, and on your chances of approval. The result is a card that fits the way you actually live.

Choose one, and the agent applies for you. If the bank has no API, it fills in the application itself.

Moments later, the card is approved and added to your phone's wallet, ready to use.

*[Use Cases → Find A Card. The request "Travel rewards, no foreign fees, and I want it now." is typed and sent. On requirements, "Connect To Bank" opens the Open Banking connection (verifying identity, assessing financial history). The spending profile appears: monthly spend by category, credit band, trips a year, cross-border share. The agent's smart criteria follow; "Find My Perfect Card" runs the search and the ranked cards appear with fit scores, expected annual value and approval odds. "Apply Instantly via Agent" steps through checking the issuer, applying through the website, form-filling, the decision and provisioning; on "added to your phone's wallet" the card flies into the wallet on a phone, with a tick and its features.]*

## 3:59 · Settle In, a concept (42 s)

And here's where Solution Studio is heading next. Settle In is a concept, built entirely on Mastercard assets.

Priya lands in New York with no US credit history. With her consent, Open Finance shares her history from her bank in Ireland, and she's approved for a card in minutes. It's in her phone's wallet before she reaches the city, ready to use at more than a hundred and fifty million places worldwide.

She sends money home, sees the exchange rate before she pays, and her mum has it in seconds. At lunch, her new statement already makes sense. When someone abroad tries her card details, Mastercard's AI stops the payment before it happens. And her first night ends with a Priceless Surprise on Broadway.

*[Use Cases → Settle In, marked "Concept · not wired yet". Priya's day runs along the top (07:55 Arrive to 19:30 Priceless); each line moves to the next moment: her Irish bank shared through Open Finance, approval with no US credit file, the card in her phone's wallet, $400 home to her mum with the rate shown first, an enriched statement and nearby essentials, a declined fraud attempt with the protections behind it (Decision Intelligence Pro, Identity Check, tokenisation, alerts), and a Priceless Surprise notification at a Broadway box office. Each moment lists the Mastercard assets behind it, marked as in Studio today or to add.]*

## 4:41 · Open to everyone, easy to set up (24 s)

Solution Studio is open to everyone who wants to innovate with Mastercard. Sign up for Mastercard Developers, clone the project, and run it. You're up and running in four steps.

And setup is just as easy. Choose auto-provision, pick the APIs you want, and Studio creates your projects and sandbox keys for you. No forms, and no copying and pasting keys.

*[The info button opens "Install & Run Solution Studio"; it scrolls through the four steps. It closes and the first-run welcome appears; "Auto-provision Keys" opens "Select APIs to Provision". The cursor rests on "Provision Selected APIs" — it is never clicked, so no keys are created.]*

## 5:05 · Close (18 s)

Mastercard is the platform for the world's economies, powering secure value exchange between people, businesses and communities. With Solution Studio, we're empowering you to innovate with us.

Helping everyone realize their potential, which is priceless.

*[Back on Home: the revolving globe and the cycling cards. The cursor fades out; the picture fades to black.]*

---

## Notes for re-recording

- **Pronunciation.** `tools/video/check_voice.py` plays the track back through Whisper; at the last run every sentence was heard as written (it reports British spellings such as *tokenisation* as differences, which is expected). Where the voice gets a word wrong, a line in `narration.json` carries a `voice` text alongside the written `say`: "Bin Lookup" so BIN is said as the word *bin*; "liv" (defined in `tools/video/lexicon-extra.txt`) so *live* rhymes with *give*; "Backs" for Bacs, "A to A Protect" and "Spending Pulse"; and "ninety-five percent" for 95%.
- **The Bacs figure.** "More than 95% of UK salaries" is Mastercard's own 2025 figure for Bacs Direct Credit. The picture in `maos` says "about 98% of UK state benefits", which has no current source, so Studio shows "Bacs pays benefits and over 95% of UK salaries" instead (`TEXT_SWAPS` in `mcos/__init__.py`).
- **Your own data shows.** The take uses whatever the running Solution Studio has: real sandbox keys give real BIN Lookup data, and with no keys the simulator answers. Find A Card's profile and scores are random each run.
- **Real merchant logos.** With Open Finance configured, Data Enrichment calls the enrichment API live, and Settle In's lunch statement uses the same results, so names, categories and logos are the API's own. The logos load from Mastercard's merchant-branding host. Where the recording machine can't reach it, `record.js` serves the same brand's logo from `tools/video/logos/` (Starbucks, Amazon, Uber, Netflix, Lyft, Apple, Target); Whole Foods Market has none there and keeps its initials.
- **Nothing is provisioned.** The welcome dialog is opened directly and the API picker is only hovered.
- **Timing.** Every action is scheduled from the voice track, so changing a sentence moves the picture with it. Find A Card reloads when selected, its bank connection takes about eight seconds, its search about five and applying about eleven, so its request is typed early, the narration leaves short pauses for it, and the wallet click is tied to "added to your phone's wallet".

## Change requests

From the review of the first draft (10 October 2026); all made in this version.

1. ✓ **Pronunciation: "BIN Lookup".** Said as *bin lookup*, with "BIN" as the word *bin*.
2. ✓ **Globe position.** Switching from Home, the Operating System tab opens around the same globe in the same place, size and rotation; it moves into the picture only as it slices into the stack.
3. ✓ **Find A Card runs to the end.** The agent applies, and the chosen card is shown added to the wallet on a phone.
4. ✓ **Pronunciation: "live".** "The way you actually live" now rhymes with *give*.
5. ✓ **The final line.** One natural sentence, "Let's build what's next, together." (a separate, slowed "together" sounded forced).

Also added: the Data Enrichment example before Find A Card, and Settle In (Priya's first day, a concept use case) after it.

From the review of the third cut: the asset list now names open finance after cyber security; the stack opens out as soon as it forms, each asset is shown on its layer as it is named, and a use case (a bank cutting fraud) is lit across the layers before the tour moves on to BIN Lookup.

From the review of the fourth cut: the Operating System is now the *platform for the world's economies*, in the picture, the tab and the voice; the asset tour gives a concrete example for each asset; a second, longer use case (a government getting money to people) runs through the layers; the Python code view is gone; the close names Mastercard as "powering secure value exchange between people, businesses and communities" and ends on "Helping everyone realize their potential, which is priceless."
