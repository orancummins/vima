# Mastercard Solution Studio — walkthrough video script

3 min 22 s · 1920×1080, 30 fps · voice: Kokoro-82M v1.0 (`af_heart`), one sentence at a time with explicit pauses · made by `tools/video/` (see its README)

The narration below is the source of truth in [`tools/video/narration.json`](../../tools/video/narration.json); edit it there and re-run the pipeline. Timings are from the current voice track. *Italic brackets* are what happens on screen.

---

## 0:01 · Mastercard's mission (18 s)

At Mastercard, our mission is to power economies and empower people. Every day, that means connecting billions of people, millions of businesses and thousands of banks, safely and simply, all around the world.

So how do you build on all of that? That's where Mastercard Solution Studio comes in.

*[Home: the Solution Studio title, the revolving dot globe and the cards cycling through use cases, APIs and bundles. No cursor.]*

## 0:19 · More than a card network (27 s)

Solution Studio helps you navigate, and innovate, across everything Mastercard has to offer. And there's a lot more to Mastercard than a card network.

There are real-time, account-to-account payments, and open finance. Tokenisation, identity, fraud and cyber security. Data and insights, loyalty, and now, agentic commerce.

We've mapped all of it as one operating system: five layers, from the network at its core, up to the ways you plug in.

*[The cursor opens the Operating System tab. The page changes around the globe, which stays exactly where it was on Home and keeps turning while the assets are listed. On "five layers" it moves into the picture as it is cut along its latitudes into five slices that settle into the stack: kernel, rails, network services, solutions, access, with the users above. The heading and the list of layers fade in beside it.]*

## 0:46 · The operating system (17 s)

Open the stack, and every layer shows the capabilities inside it. Each area lists the products behind it, and the orange markers show what you can try live, right here in Studio.

Let's take BIN Lookup, which tells you all about a Mastercard card range. Every API is just one click away.

*[The stack opens. The Kernel layer is selected; its areas list on the right, and the cursor rests on an orange marker. Franchise & rules opens; the BIN Lookup card expands to "Try it in Solution Studio", and the cursor clicks the BIN Lookup API button.]*

## 1:03 · A live API (16 s)

Each API comes pre-wired, with authentication and request signing handled for you. Pick a card range, hit send, and there's the response. The issuer, the product, the country, in about a second.

When you're ready, the same call is waiting as Python code for your own app.

*[The APIs tab opens on BIN Lookup. The cursor picks "Lookup BIN" and clicks Send; the request and a 200 response appear. "View Code" opens the ready-to-run Python.]*

## 1:19 · API bundles (22 s)

APIs are even more powerful together, so we've grouped them into bundles built around real business problems. Merchant Resolution, for example, combines Consumer Clarity, Merchant Identifier and Places. So cardholders always recognise who they paid, and fewer disputes ever start.

Every bundle walks you through how the APIs fit together, step by step.

*[The code view closes; the API Bundles tab opens on Merchant resolution: header, hero visual, what you can do. The page scrolls to "How the APIs fit together" and the walkthroughs.]*

## 1:41 · Data enrichment (17 s)

Then there are use cases: complete experiences that bring the APIs to life.

Let's start simple. This is what a bank statement really looks like. And this is the same data after Mastercard enriches it. The real merchant, its logo, a proper category, and where to find it.

*[Use Cases → Data Enrichment. Raw statement lines such as `SBUX 00654321 CARD 12345` and `AMZN MKTP US*MK7G3B2X1` sit with "Merchant unknown". The cursor enriches the first two one at a time, then "Enrich all": each becomes the merchant's name and logo, its category, its website and, where the data has one, its location.]*

## 1:58 · Find A Card (47 s)

Find A Card goes further. It shows how an AI agent could find the right card for you.

You start by telling the agent what you want, in your own words. Then, with your permission, it connects to your bank through Open Finance, and learns how you really spend. Where the money goes, how often you travel, and how much you spend abroad.

From that, it builds its own search, and scores every card on value, and on your chances of approval. The result is a card that fits the way you actually live.

Choose one, and the agent applies for you. If the bank has no API, it fills in the application itself.

Moments later, the card is approved and added to your phone's wallet, ready to use.

*[Use Cases → Find A Card. The request "Travel rewards, no foreign fees, and I want it now." is typed and sent. On requirements, "Connect To Bank" opens the Open Banking connection (verifying identity, assessing financial history). The spending profile appears: monthly spend by category, credit band, trips a year, cross-border share. The agent's smart criteria follow; "Find My Perfect Card" runs the search and the ranked cards appear with fit scores, expected annual value and approval odds. "Apply Instantly via Agent" steps through checking the issuer, applying through the website, form-filling, the decision and provisioning; on "added to your phone's wallet" the card flies into the wallet on a phone, with a tick and its features.]*

## 2:45 · Open to everyone, easy to set up (22 s)

Solution Studio is open to everyone who wants to innovate with Mastercard. Sign up for Mastercard Developers, clone the project, and run it. You're up and running in four steps.

And setup is just as easy. Choose auto-provision, pick the APIs you want, and Studio creates your projects and sandbox keys for you. No forms, and no copying and pasting keys.

*[The info button opens "Install & Run Solution Studio"; it scrolls through the four steps. It closes and the first-run welcome appears; "Auto-provision Keys" opens "Select APIs to Provision". The cursor rests on "Provision Selected APIs" — it is never clicked, so no keys are created.]*

## 3:07 · Close (15 s)

Mastercard is powering commerce for people, businesses and economies everywhere. With Solution Studio, we're empowering you to innovate with us.

Let's build what's next…

… together.

*[Back on Home: the revolving globe and the cycling cards. The cursor fades out. A full pause before "together", spoken slower as the closing word; the picture fades to black.]*

---

## Notes for re-recording

- **Pronunciation.** `tools/video/check_voice.py` plays the track back through Whisper; at the last run every sentence was heard as written (it reports British spellings such as *tokenisation* as differences, which is expected). Where the voice gets a word wrong, a line in `narration.json` carries a `voice` text alongside the written `say`: "Bin Lookup" so BIN is said as the word *bin*, and "liv" (defined in `tools/video/lexicon-extra.txt`) so *live* rhymes with *give*.
- **Your own data shows.** The take uses whatever the running Solution Studio has: real sandbox keys give real BIN Lookup data and enrichment logos, and with no keys the simulator answers. Find A Card's profile and scores are random each run.
- **Nothing is provisioned.** The welcome dialog is opened directly and the API picker is only hovered.
- **Timing.** Every action is scheduled from the voice track, so changing a sentence moves the picture with it. Find A Card's bank connection takes about ten seconds and applying about eleven, so its clicks start early and the wallet click is tied to "added to your phone's wallet".

## Change requests

From the review of the first draft (10 October 2026); all made in this version.

1. ✓ **Pronunciation: "BIN Lookup".** Said as *bin lookup*, with "BIN" as the word *bin*.
2. ✓ **Globe position.** Switching from Home, the Operating System tab opens around the same globe in the same place, size and rotation; it moves into the picture only as it slices into the stack.
3. ✓ **Find A Card runs to the end.** The agent applies, and the chosen card is shown added to the wallet on a phone.
4. ✓ **Pronunciation: "live".** "The way you actually live" now rhymes with *give*.
5. ✓ **The final line.** "Let's build what's next…", a full pause, then "together." on its own, slower, with a falling tone.

Also added: the Data Enrichment example before Find A Card.
