# Mastercard Solution Studio — walkthrough video script

2 min 52 s · 1920×1080, 30 fps · voice: Kokoro-82M v1.0 (`af_heart`), one sentence at a time with explicit pauses · made by `tools/video/` (see its README)

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

*[The cursor opens the Operating System tab. The Home globe glides across into the picture and keeps turning while the assets are listed. On "five layers" it is cut along its latitudes into five slices that settle into the stack: kernel, rails, network services, solutions, access, with the users above.]*

## 0:46 · The operating system (18 s)

Open the stack, and every layer shows the capabilities inside it. Each area lists the products behind it, and the orange markers show what you can try live, right here in Studio.

Let's take BIN Lookup, which tells you all about a Mastercard card range. Every API is just one click away.

*[The stack opens. The Kernel layer is selected; its areas list on the right, and the cursor rests on an orange marker. Franchise & rules opens; the BIN Lookup card expands to "Try it in Solution Studio", and the cursor clicks the BIN Lookup API button.]*

## 1:04 · A live API (16 s)

Each API comes pre-wired, with authentication and request signing handled for you. Pick a card range, hit send, and there's the response. The issuer, the product, the country, in about a second.

When you're ready, the same call is waiting as Python code for your own app.

*[The APIs tab opens on BIN Lookup. The cursor picks "Lookup BIN" and clicks Send; the request and a 200 response appear. "View Code" opens the ready-to-run Python.]*

## 1:20 · API bundles (22 s)

APIs are even more powerful together, so we've grouped them into bundles built around real business problems. Merchant Resolution, for example, combines Consumer Clarity, Merchant Identifier and Places. So cardholders always recognise who they paid, and fewer disputes ever start.

Every bundle walks you through how the APIs fit together, step by step.

*[The code view closes; the API Bundles tab opens on Merchant resolution: header, hero visual, what you can do. The page scrolls to "How the APIs fit together" and the walkthroughs.]*

## 1:42 · Find A Card (34 s)

Then there are use cases: complete experiences that bring the APIs to life. This is Find A Card. It shows how an AI agent could find the right card for you.

You start by telling the agent what you want, in your own words. Then, with your permission, it connects to your bank through Open Finance, and learns how you really spend. Where the money goes, how often you travel, and how much you spend abroad.

From that, it builds its own search, and scores every card on value, and on your chances of approval. The result is a card that fits the way you actually live.

*[Use Cases → Find A Card. The request "Travel rewards, no foreign fees, and I want it now." is typed and sent. On requirements, "Connect To Bank" opens the Open Banking connection (verifying identity, assessing financial history). The spending profile appears: monthly spend by category, credit band, trips a year, cross-border share. The agent's smart criteria follow; "Find My Perfect Card" runs the search and the ranked cards appear with fit scores, expected annual value and approval odds.]*

## 2:16 · Open to everyone, easy to set up (22 s)

Solution Studio is open to everyone who wants to innovate with Mastercard. Sign up for Mastercard Developers, clone the project, and run it. You're up and running in four steps.

And setup is just as easy. Choose auto-provision, pick the APIs you want, and Studio creates your projects and sandbox keys for you. No forms, and no copying and pasting keys.

*[The info button opens "Install & Run Solution Studio"; it scrolls through the four steps. It closes and the first-run welcome appears; "Auto-provision Keys" opens "Select APIs to Provision". The cursor rests on "Provision Selected APIs" — it is never clicked, so no keys are created.]*

## 2:38 · Close (14 s)

Mastercard is powering commerce for people, businesses and economies everywhere. With Solution Studio, we're empowering you to innovate with us.

Let's build what's next, together.

*[Back on Home: the revolving globe and the cycling cards. The cursor fades out; the picture fades to black.]*

---

## Notes for re-recording

- **Pronunciation.** `tools/video/check_voice.py` plays the track back through Whisper; at the last run every sentence was heard as written (it reports British spellings such as *tokenisation* as differences, which is expected).
- **Your own data shows.** The take uses whatever the running Solution Studio has: real sandbox keys give real BIN Lookup data, and with no keys the simulator answers. Find A Card's profile and scores are random each run.
- **Nothing is provisioned.** The welcome dialog is opened directly and the API picker is only hovered.
- **Timing.** Every action is scheduled from the voice track, so changing a sentence moves the picture with it. Find A Card's bank connection takes about ten seconds; its clicks are placed early so the spend profile lands on "where the money goes".

## Change requests for the next version

Noted after reviewing the first draft (10 October 2026); not yet made.

1. **Pronunciation: "BIN Lookup".** Say *bin lookup*, with "BIN" as the word *bin*, never spelled out as B-I-N. It is spoken in the Operating System section ("Let's take BIN Lookup…").
2. **Globe position.** The globe in the Operating System tab sits in a different place from the Home globe, so the switch between the tabs looks disjointed even with the glide. The two should line up so the transition reads as one continuous globe.
3. **Find A Card runs to the end.** Carry the use case through to its last step, so the chosen card is shown loaded into the wallet on a phone, rather than stopping at the ranked results.
4. **Pronunciation: "live".** In "The result is a card that fits the way you actually live" (Find A Card), the narrator says *live* like the adjective in "live music" (rhymes with *five*). It should be the verb, rhyming with *give*.
