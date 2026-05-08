---
title: "Payments in the Sharing Economy"
subtitle: "Panel discussion on the unique challenges of marketplace and platform payment architectures."
publishDate: 2019-10-15 00:00:00
img: /assets/sharing-economy-thumb.jpg
img_alt: Payments in the Sharing Economy panel at PAYMENTSfn 2019
description: |
  Panel discussion at PAYMENTSfn 2019 exploring how payments infrastructure enables and shapes the sharing economy.
tags:
  - Conference Panel
  - Payments
  - Fintech
---

## PAYMENTSfn 2019 Panel Discussion

At PAYMENTSfn 2019, I joined fellow payments professionals to discuss how payment infrastructure contributes to and enables the sharing economy.

### Key Discussion Points

**Platform Economics** - How two-sided marketplaces like delivery platforms, ride-sharing, and accommodation services depend on seamless payment flows between multiple parties.

**Trust Through Payments** - The role of payment systems in building trust between strangers in sharing economy transactions. Escrow-like mechanisms, instant payouts, and dispute resolution as enablers of peer-to-peer commerce.

**Cross-Border Complexity** - Managing payments when platforms operate across multiple countries with different currencies, regulations, and consumer preferences.

**Instant Gratification** - How the expectation of real-time everything (booking, payment, service, payout) challenges traditional payment settlement timelines.

**Fraud in Marketplaces** - Unique fraud vectors in sharing economy platforms where both sides of a transaction could be bad actors, and how payment data helps identify suspicious patterns.

The sharing economy has fundamentally changed how people think about ownership, work, and transactions—and payments infrastructure is at the heart of making it all possible.

[Watch the panel on YouTube →](https://www.youtube.com/watch?v=KvCVofBzCAc)

<details>
<summary>View transcript (auto-generated, multi-speaker)</summary>

> Auto-generated YouTube captions, cleaned up. Speaker labels per turn are inferred from the dialogue (each panelist introduces themselves; later turns reference their company — Spring/Ebor for Dan, PedidosYa for Mathias, Patreon for Michelle, general industry for Fareed). A few `[?]` markers indicate spots where the auto-caption was unclear. For the canonical version, watch the video.

*[Music]*

**Peter:** Terrific. Hi, so — you may remember me from a few moments ago. I just like to introduce a panel. So you've already heard from Michelle of course, but would love to hear just a quick intro from everybody if you don't mind — just which company you're with, and what you do there. So Dan, if you don't mind starting?

**Dan:** Thanks so much, Peter. So my name is Dan Zee. I spent most of the last five years building a fashion e-commerce marketplace called Spring, where you can shop from brands large and small — as large as Nike and Michael Kors, as small as single-shop Nolita-in-New-York–type brands — so figuring out payments flows across that. And then just as of a week ago I have just joined Ebor, so excited to tackle some more scale through that.

**Mathias:** My name is Mathias. I work at PedidosYa, which is something difficult to pronounce in English. We started as a food delivery company, but right now we are delivering anything. We are not trying to compete with Amazon, but we started with pharmacy — that I heard about, talking about that — electronics, and anything in the future. So we started with payments three years ago. It's been stopping for us. Anyway. *[laughs]*

**Michelle:** Michelle Voltea. I'm the Vice President of Payments and Risk at Patreon, and for whoever wasn't here this morning — Patreon: the membership platform for artists and creators. So I'm focusing on scaling and bringing them globally, both from a paying and a payout standpoint.

**Fareed:** Hi, I'm Fareed. I've been in the payments industry for a long time, most recently helping older [?] scale payments as they expand globally, both for payment and for [payouts].

**Peter:** Terrific. Well, thanks everybody. And like I mentioned before, definitely glad to take questions from the audience, so feel free to raise your hand or just simply email me at pm@spreedly.

Dan, I'd like to start with you actually. So a lot of our conversations have been about merchants and about marketplaces. Your experience has been specifically in the last 5 years around marketplaces — so when we're talking about scaling payments, what unique characteristics do you see for scaling payments within marketplaces?

**Dan:** So I think when building a marketplace, one of the trickiest considerations is to figure out how much leverage you have over your suppliers. You think about one extreme where you have individuals as your suppliers — maybe you have a car driver acting for themselves — and at the other extreme you have Nike. You have these hundred-billion-dollar organizations. And I think figuring out how are you going to get money from your customer, and then get it to that merchant partner, and how much work is required from that partner.

So I think for us in the beginning, bringing on the smaller merchants, it was really easy to say, "you know what, let's just do merchant onboarding." I think this morning it might have been Carrie talking about how easy merchant onboarding has gotten, if they're willing to do it. But then as you start getting into bigger and bigger suppliers, you might start running into some of those organizational roadblocks where they're not actually willing — even if it's easy, there's still internal politics or organizational challenges. So actually, for us, scaling: one of the biggest challenges was, how can we have a payments infrastructure that allows us to onboard the big enterprise suppliers without necessarily having to wait for their own internal organizational approvals to go through? So figuring out some creative workarounds through issuing virtual credit cards and so on — which, if the conversation goes there, we can talk more about.

**Peter:** Okay, great. So Michelle, actually I was thinking a little bit about that with — in a marketplace model where you have creators and artists on one side, was there any kind of education process where you had to educate the artists and creators on payments and the importance of that? Or did Patreon in general have to do that in order to get the two sides of the market?

**Michelle:** Yeah, so I think the way we think about it is, we actually control the whole payment-checkout experience for creators. So the patron experience is completely divided from the creator experience.

It's been a challenge from a payout standpoint, because what we do is we have three different options for payouts: we offer ACH, we offer PayPal, we offer Payoneer. And then we just educate them while they're pricing — the different pricing models and different limits, etc. — and then let them choose. In the beginning, we just put the logos up and just go for it, and then we were like, "oh, you have so many questions! They've never done this before! How do we also understand that onboarding experience for them?" — because we've kind of pushed it off to our partners. So now we started building Help Center articles, screenshots, understanding that experience, and starting to own that experience a little bit more, and streamlining it from a Patreon perspective. So it's been an evolution. We're still not done — nowhere near.

**Peter:** Okay, great. So Mathias — I mentioned, you have similar scenarios where you've got multiple sides. With the delivery side, you have a restaurant, you've got the deliverer, and also the recipient, the consumer themselves. So how do you deal with that, where there's maybe three sides to the market?

**Mathias:** Yeah, exactly. It's been like a huge travel [?], actually. Internally and externally. Internally in the company, we had to educate — I'm saying "educate" not because I knew about it, right? First *I* learned, and then I tried to take it. For example, something as obvious as, talking about customer support: "people in the company, do not ask for the credit card number by phone, please." That's an example of things that we had to talk about inside the company.

And then you have externally, in Latin — as Catherine [?] was talking about — everything is new and everything is not so trusted. So you have to talk with restaurants and assure them they're gonna have the money someday. Yeah, actually, for most cases it's in the next day, but they don't trust it — they want the money right now. I mean, for years and years they delivered food and got the money directly from the client, and actually the rider, the deliverer, was an employee of the restaurant. So now that we're offering the whole platform, it's a huge job for us to convince them. We have also an onboarding process for restaurants because we have to explain how they are gonna get the money, how the orders come, how we manage the order modification, for example. And yeah, it's a huge process that involves a lot of learning from multiple sides.

**Fareed:** Very interesting insights from everybody. In fact, my answer's slightly technical and kind of goes back to what Kathleen [?] was alluding to earlier. As scaling payments globally — especially if you look at it from an international perspective — is making sure that you support multiple payment methods, I think that's a big one. It's also ensuring that your downstream providers can scale with you, too.

Often when you launch as a new startup you go with whoever's willing to accept you, right? Because there's not a lot of bargaining power, and the classic acquirer/ISO is not going to touch you. I remember Amazon Payments was the only one that supported Kickstarter when they started, because nobody wanted to take on the risk of a crowdfunding platform. So I think as startup ecosystems evolve, you're going to find that you typically sign up with somebody who's willing to take you on, and then you also sometimes outgrow them, right? So it's important to make sure that your downstream partners are able to scale with you. I think that's an important aspect.

**Mathias:** I would like to add that they are able and they *want to* — because something that happened too much for us is that the infrastructure in many countries — in Uruguay, or small countries — they don't want to, they don't *need* to, because they have a mindset of "this is what we have, and this is what we need." So you have to convince them. Like you were saying previously with the Mexican gateway providers, we still are not able to convince them that recurring payments are something that they need. They say, "no, we don't have that. Just call me once a month."

**Fareed:** We can team up on a strategy! Building teams one panel at a time.

**Peter:** That's great.

**Fareed:** So just to add to that: I think the other thing — from a money angle — that you need to take care of, is try and make sure that you get settled sooner than is the norm, because this is an area where you do run into cash flow issues as you scale. So it depends on managing that settlement window very well.

**Peter:** Great. Yeah, and that settlement plays into the idea of trust. I know you're speaking to trust. Dan, when you're thinking about the marketplace that you built at Spring, how important was that building of trust at the beginning? Between buyers and sellers, or with the sellers in particular?

**Dan:** Yeah, I think — sorry, I'm still hanging on to Fareed's last word about cash flow because you've just taken me back to a lot of PTSD on that front. With trust this comes in as well: merchants want to get paid before they ship something. There's different ways that you can satisfy that, but as a marketplace, you have to figure out how much risk are you willing to take on, how much you're willing to intermediate that transaction. Because you want to create a great experience for the customer on the one side — where they know they're gonna have a consistent phone number to call for support, or they have an email address — they don't want to necessarily go directly to 1,500 different merchants that are selling. But on the merchant side, most merchants aren't going to ship until they have that money. So for example, can you afford to do capture-after-ship as a marketplace?

That's something that we actually two years in changed our point of view on. Right? We started by saying to our supplier partners that they should ship and then we'll capture. Ultimately we needed to change that to capture upfront, because we were losing out — we were having chargebacks happen later, and they were asking, "well hold on, how come I have this happen?" So yeah, I think managing that cash flow and then also managing that trust together were really tightly linked for us.

**Michelle:** If I can get on that train, I'll also kind of share a story around trust and cash flow. So I think I mentioned earlier, we process payments on the first of the month, so 100% of our payments are processed on the first of the month — our renewals. Our creators over the last five, six years have started to depend more and more on the income they earn on our platform as kind of their paycheck. Most of these artists were monetizing in different areas, and Patreon has consolidated a lot of that.

So the way our team thinks about it is, this is our creators' paycheck. So we process payments on the first, and then we auto-payout on the fifth of the month on your balance, essentially. And that's kind of the order of operation. But if you're a creator and you want to pay out on the second, third, you can. But we say, "hey, we process on the first. On the fifth we feel like, with these two rounds [?] of retries, it's pretty solid. By the 15th of the month, it's like a very small percentage change of what we're going to capture, and obviously by the end of the month we finished our retry strategy." So that's kind of what we usually tell our creators.

So on February 1st — I don't know if y'all, some of you remember, right before, a few weeks before that, MySQL had an update, and we use MySQL to run our databases — and so we wake up on January 31st (sorry, the 28th) and we start doing all our bill aggregation process: we aggregate all our bills, we get them ready for processing, and Feb 1st we start processing.

We notice that our billing engine is lagging, like, "oh, that's weird. This is usually done in a two-hour process, it's been four, five, six hours, it's still not done. Oh, we are not gonna make the first." And so it got to a point where, if we couldn't process all our payments before the fifth, we essentially did not make good on our promise to our creators. And this is their paycheck. Imagine — what I told the company, I was like, "imagine if I just forgot to press the payroll button and none of you got paid. That's not cool, right?"

And so what we had to do is, we quickly realized there was an issue with our database — scaling, big issue — and there were some issues on our side, plus the MySQL update; there was a lot of calamity of events that happened. So what we had to do is build an Advanced Payout tool overnight. So my engineering team and product team spent exactly 24 hours building an Advanced Payout tool. What we did is, we estimated 90% of what we think they're going to make before the fifth of the month, and we advance-paid that out to creators who needed it. It was insane. There were bugs in it, we had to fix, there was tons of cleanup. But we needed to place something in 24 hours, and it was really important to have the cash flow available to be able to react fast and sort of keep our promise — because we really didn't [otherwise]. But then March, for us, everything went well. So just — yeah.

**Peter:** That's great, thank you. So I mentioned, Dan, you had — you have first of the month, that's like the big time for you — I'm 36 hours, are you really good?

**Dan:** Okay, we were not scheduling payments — for first of the month, I won't be here.

*[laughter]*

**Peter:** Okay. So now Mathias, for yourself — I mean, you have deliveries, a lot of those deliveries are happening late at night, right? So how are you able to scale up and make sure customer service is there, or you're able to process those transactions, because they're not 9-to-5, are they?

**Mathias:** Well, one thing I learned all is that hungry people are angry people. The more you move the wait, it's incredible how much they depend on you. Once a woman called us and said that their children were starving because of us. I was like, "well, don't you have rice?"

*[laughter]*

Well — yeah, our peak hours are lunch and dinner time, especially soccer matches. In Latin, everybody gets to get together and they order even more food, and with even more desperation, because they want the food before the game or in the halftime, but not during the game. So it's extremely difficult, and the infrastructure that we need and the customer service that we need has to be optimized to the maximum.

The other thing that's important is to have an internal communication completely smooth when you have promotions, discounts, or special days for a specific card. We have a monitoring system — doesn't work perfectly, but it works — and sometimes we noticed a peak in usage of a specific card, or a specific bank-issued card, and we were like, "okay, we're having an attack — what's happening?" And it was that the marketing team launched a campaign, and they didn't tell us. That's important for the availability of the service in terms of technical terms, and in terms of operations also, business.

**Peter:** Yeah, that collaboration is definitely a topic I want to come back to. But first, Dan — I mean, we heard from Catherine [?] about Singles' Day in China. With Spring, big times of the year as well. So how would you deal with those big scaling times?

**Dan:** So Spring, as a fashion marketplace, increasingly found customers in China — were very excited to have access to a lot of the American brands, to Catherine's point. So Singles' Day, and then Black Friday of course, were our two biggest days. I would say two things to call out from our perspective.

One is that it's nice in commerce that it is somewhat predictable, so you can plan. And so we would start planning for Black Friday cross-functionally in May, and spend half the year thinking about it. It was almost as if our entire tech roadmap was almost set, because that is our peak stress day — how can we build the things for that? So for us, it was making sure we had the right vendors and partners. One tax-computation vendor that shall remain nameless — but you probably all use, because they have a bit of a monopoly — decided to go down for us on Black Friday about four years ago, and so we had to very quickly, in about an hour, figure out: "how do we just skip collecting sales tax for everyone, and just figure it out later, and remit whatever we have to remit, but just let's get the orders through?" I don't know if any of you were affected by that same outage of that same nameless vendor. So making sure you have those vendors in line.

And then for us — sorry to harp on cash flow — but as a marketplace that moved to a two-transaction model, where we were collecting funds from customers and then placing a separate transaction with our brand partner like Nike, we needed to have typically about five or six business days of float. So if you think about a day like Black Friday, where you're gonna be doing 10x or 15x or 30x your normal day — maybe even 100x — you start looking at your balance sheet and your cap table and you're like, "oh my goodness, this is like as much money as we've raised." So figuring out what is a good cash flow strategy, and how can you maybe get some creative partnerships to allow — especially if any of you are in that two-transaction marketplace world, where you have to pay out your suppliers and float some of that cash — making sure you have a capital planning process as well.

**Fareed:** Line of credit?

**Dan:** Yeah, I wish we could have.

**Peter:** Now, Fareed, do you see, with all — are there peak times as well? And how do you handle that?

**Fareed:** I think all online businesses really plan around peaks. We have our peaks, and strangely they're a bit different in different countries. For example in Australia we have a four-day peak, and in India it's typically a weekend peak. And something that I think most of us — I think there are a lot of technologists and programmers in the room — we dislike doing, is throttling. But I think sometimes as you scale a payments business, it's better to throttle, because in payments, you don't want your transaction going into the ether — you want to make sure that you have actual closure on the transaction, either an approval or a decline. Not knowing what happened to the transaction is very painful, and leads to a lot of CS issues. So I think I would certainly want to obviously try and do my sizing right and make sure I can handle peak volumes, but if I can't, I want to be able to make sure that we can fall back on some throttling.

**Mathias:** Sorry, can I add one more thing? Another thing that we have trouble with — and maybe it's a local thing for Latin — is that not only do we have to be careful in peak times when accepting payments, but also with refunds and chargebacks. Because depending on the bank and the country, sometimes refunds take a lot of time. And again, angry people: "you take my money in ten seconds, but it takes you four days to return it to me." And it gets worse when you get a chargeback because the person didn't like what they received — so it's an angry refund: "give me back my money right now." So you have to take into account that you're gonna be accepting transactions and also refunding them very quickly when the restaurant rejects the order, or even in a time frame, I know, of thirty days.

**Peter:** Great points.

**Fareed:** Actually, anecdotally, there is a bank who shall remain nameless in India whose largest "merchant" was refunds — that they never returned to customers — until the regulator actually made it mandatory to process refunds. This was seven, eight years ago. It's a much happier state now, but back then, refunds could actually go to bottom lines.

**Peter:** So I have to remember never to do business with a company named Nameless! Okay, so that's fair.

So the bad side of scaling as well is fraud. How are you dealing with fraud at scale? Michelle, curious your thoughts there. How are we dealing with fraud at scale?

**Michelle:** Anybody — did anybody use Smyte? No? Okay. Smyte was our bot detector, and Twitter bought them and shut them down in less than 24 hours, and did not alert any of the customers. It's great. Right before 4th of July weekend. It was awesome. *[Nameless social-media company that — don't know why.]* Well, I have told them, I will tell them — I was just like, "how could you do that to so many people?"

Luckily we had others — we didn't have redundancy on the bots — and it took them about two days to figure out that we were using Smyte and that Smyte was down, and we got attacked with about three million dollars worth of ATO fraud. It was great. *How* do I explain that to my executive team? But it also taught us a really good lesson: to have redundancy, to use many data points, don't rely on one. And so our fraud model is mostly built on a lot of third-party vendors that we use, and then also we just deployed about two weeks ago our own machine learning model, and that came out of our July event. It was great in the sense that — well, it was bad in the sense of the loss that we had, but it was great in the sense that it allowed me to say, "hey, we cannot depend only on third-party vendors. They're great inputs. We need to start thinking and acting on ourselves, and rule-based doesn't always work." So now we're integrating all of that together to hopefully be better and learn from that mistake, and hopefully scale.

**Dan:** Great. I think fraud is such an arms race. I think you have to take an honest look at the stage of your company and where your core competencies are, and decide: is fraud something that you're gonna be really good at? And if so, at what stage? When is it right to start building that machine learning model versus, "you know what, we have just hired our tenth engineer, or we had our 20th engineer, and we're not gonna be good at this compared to what's out there" — and saying, "you know what, let's find a partner who we can integrate with."

So having now implemented two different fraud vendors — one that was a complete failure and one that was great — but you know, just looking at what is an acceptable cost structure: can we afford half a point of our top line and just outsource this for while we scale for the next couple of years? And then say, "okay, when we actually need that half a point to be 0.1, or five basis points, then let's go." But I think just being honest with yourself about where your capabilities are and what stage you're at — and hopefully not getting to the point where you're getting letters from Visa and Mastercard saying you have $300,000 in fees on top of the chargebacks. Oh yeah, that's a nice tirade about chargeback programs.

**Fareed:** Let's try to — to what Dan says, I think it's important to know when to make the right investment into fraud detection internally. It is a science at the end of the day, and it's really easy to build ML models. There are various algorithms out there, and it's very tempting for a techie to actually try and say, "hey, I can do this." But it really depends on the data, it really depends on how well your systems have learned. So you need to probably, like Dan said, be prepared to spend 10, 20 basis points for the next two years of your life as a startup in the space, or even an established company trying to do business in a new region, just to make sure that you don't get slammed.

There is, apart from financial losses, there is significant reputation loss. And the other bit of advice that — having gone through it a couple of times — is *redundancy*, like Michelle was saying. So it's good to have more than one provider or vendor, and you can figure out what kind of volumes you dial up or dial down. But it's good to have more than one available on tap.

**Mathias:** I completely agree with everybody. What we have right now in PedidosYa is a complex network of third parties [and] internally-built tools, and we are still struggling. Because we are never going to be able to solve the fraud problem for everyone — if anyone does, please tell us the secret.

But what I wanted to add is that this is my favorite topic to argue about in my company. I get invited — actually, the people stopped inviting me to the meetings, because they knew. I was like — but I took the flag of "let's keep fraud" — no, no, I mean, fraud is an important topic, and many people in my company didn't take that into account. And even when, after I don't know two years of effort of the team building the fraud detection algorithms, when we got to a good percentage — I mean, when the fraud was really low — likely [?] in the payments team and the payments-and-fraud team we were really happy, we were congratulating ourselves for a job. And I remember a manager, that shall remain nameless, that said, "why do we have so many people in this team, and why are we spending so much money on the providers, if the fraud rates are so low?" It was like, "no, let me start again with every argument we had three years [ago]." And I actually came to the point — I was very angry, and now I'm laughing — but no, I came to the point that I said, "do you want me to turn it off? Let's see."

*[laughter]*

**Michelle:** Something I've seen that's worked really well — because I think from a fraud and risk perspective, they're the unsung heroes. They — at least my team and teams that I've led in that space — have always been like, "no news is good news." But did we get rewarded on no news? And how do we show the work that we've done, and how do we showcase that, so we don't have to answer that question as to "why do I have 10 engineers working on our fraud models?"

So one of the things I've done at another company, that I'm hoping to kind of do here as well at some point, is a monthly threshold of funds that we feel would be okay to lose. So, say — I don't know, I'm just making up a number — one percent. We would establish that one percent baseline, and obviously, say having one percent fraud is a lot [?] — but just making it easy — and reserve those funds in the P&L. And then if whatever the delta is, that team gets to keep, and then reinvest into whatever new thing they wanted to think about that's outside of business as usual. And that's really helped them, because they're like, "okay, we kind of are in control of our investments. If we can really do a really good job, we get smarter around this, and we can keep that delta of that budget and reinvest it in new teammates, or get into different technologies, or whatever it is." So I don't know — for me, that's worked in past teams, and I'm thinking about doing that here as well.

**Fareed:** Coming back to the team on scaling payments and the related fraud that you see — I think it's important to try and get a handle on a metric that is really hard to get a feel for, which is **false positives**. The really only way to do it that I know of — and Michelle, if you know anything else — is to try and do a sample, and try and understand where you are at, to do a litmus test. And I think it's important to keep that metric, that'll let you figure out how tight your controls are. You really don't want to be in a position where you're scaling, and you're actually still turning away legitimate customers.

**Michelle:** We also look at CS [customer-service] complaints, so if anybody complains that the card was declined. Yeah, I haven't found a perfect solution for it either, sorry.

**Peter:** Okay, great. Dan, jump in?

**Dan:** Finding false positives, measuring false positives, is hard. I just wish to emphasize theirs — I've never seen a great way of doing it.

**Peter:** Okay, great. So I'm gonna open up for questions from the audience in just a second, but going back to Michelle — one of your takeaways from this morning was about collaboration between teams internally. And also, on your point now about motivating your team — curious of how folks in the panel have worked with other teams outside of the pure payments team. Like infrastructure, and dev, and finance. I know we've got two accountants, I think we heard, this morning in the audience. So how working with finance is important too, right? How do you foster those kind of relationships to ensure that when you are scaling — when you do have that first of the month, or the Singles' Day, or whatever it is — that you've got those foundations in place across the organization?

**Mathias:** I'll start with that one. I think there are many developers here, and one of the challenges that we have as payments developers is to explain to other developers how huge the unknown is in our code. There are some parts of the code that you control absolutely, but whenever you lose control — whenever you call a provider, and what comes back: you can get an "accept" response, a "reject" response, or no response. "No response": is it still good? But when you get something that you didn't expect, how do you interpret that? How do you work with them?

So I had — also had — many arguments. It seems like I'm an angry person. I also have had many arguments with developers that said, like, "it's easy, just unit-test and do testing." But you never know, you cannot unit-test — you can be prepared to a certain level, but you never know what happens. So that's about the relationship between my team technically with other teams — it's like, we are really different.

**Fareed:** Just to add to that, I think it's really important for folks in the payments teams to really be invested either as honorary members, or somebody who really keeps office hours for compliance, for legal, [for] information security teams. I think [those are] really critical to you, and product, from an experience [perspective] — because no matter how great your rails are, if your experience sucks, the whole thing is a goner anyway. So I would certainly make sure that we keep regular office hours for these cross-functional teams that play a huge part in keeping us legit, honest, and doing a great job for our customers.

**Dan:** I should say, as a product manager, similar to office hours: I think just being present for those teams in general. I think there's two other ways besides office hours that I've seen be successful. One is having a good responsive bug-fix process. I know it's so tempting to let bugs slide away, but I think being quick and responsive to a team member who's serviced a bug is a great way to build that trust. And then the second one is, making sure that you're dedicating a portion of your time to internal tools — which again often make it to the bottom of the roadmap — and they're often less about the business case and more just about the trust and collaboration that they engender by building that tool that then saves someone the three hours, or twelve hours, of spreadsheets they would have to do.

**Michelle:** Yeah, I agree with all that's been said, and I can add a little more. I think a large part of my role is just an internal evangelist, of helping each team understand the different things that we're doing and how it impacts them, and how the different things that they do impact us. So that's always been a huge part of my role.

A lot of what I do — I do all employee onboarding, so I educate all employees on "what does the payments team do? We are a payments company, but we're not." And go through that. I spend a lot of time with finance — a lot of time with finance — you know, we're working on being global, we're starting to set up local offices, and they're like, "why do we need legal entities, why do we need revenue centers?" I'm just kind of going through that whole process with them, and then showing the different types of providers out there that you need a revenue center for, or not, and how do you think about it, what is the strategy.

I spend a lot of time with what we call "community happiness": that's our call-center team and contact support. Anytime we do any change, we walk them through it, we do a lot of lunch-and-learns. We spend a lot of time educating the company. And then also we bring our partners — we open it up to "hey, you want to do a lunch-and-learn at our company?" — and tell them what you do for us. So that also kind of helps. But it's really keeping a line of communication across all the different areas. And I think the thing that I've taken as my responsibility as head of payments is to make sure that every team knows the impact that they have, or that I will have impact on them. I don't expect them to all know that.

**Peter:** Great, thank you. So we are coming up on time, but I do want to make sure that we have a chance to get some questions from the audience. So anyone have a question?

I did get one through — Adam, you referenced a good fraud experience with the vendor and a bad one. So could you tell us about the bad one and give us all the details?

*[laughter]*

No, I understand, but on the [other side] — what is a good [experience]? Can you walk through a little bit what a good experience with a fraud vendor looks like for people in the audience who may be thinking about tackling that problem?

**Dan:** A good experience is one where your expectations become reality, is the simple answer. And I think for us, the bad experience was the fraud rates that were way, way, way in excess. We did cross that one percent threshold, something was wrong. And so then I think being willing to pay for a number that's a lot less than 1%, but still non-trivial — but knowing that it's predictable, and having that predictable line item, so that our CFO knows in his annual plan that this is what's gonna happen, and we just work around it. I think fraud is so unpredictable, but getting to predictability was what made the second experience better, even if it was expensive.

**Peter:** So you reduced fraud, but you also feel like the customer experience stayed largely unchanged? I know false positives are hard to track, but sort of thinking about the whole overall experience and the trade-offs?

**Dan:** Yeah, it's tricky, because a lot of your good customers will never know about your fraud systems, and so I don't know of a good answer for that. I think it is one of these unsung-hero things, where you're not really creating a better customer experience by having a better fraud team, besides by keeping your business in operation and continuing to deliver the product that they want.

**Michelle:** Yeah, I would also kind of counter that a little bit. I think from a marketplace standpoint, protecting your customers from ATOs, account takeovers, and not just transaction fraud, but overall account security — that's gonna say a lot to, in my case, the patron. And then also we're super susceptible to account takeover, just because they know that we pay out creators and there's a balance. So if they can have a creator account, they switch the payment method, they can go home with all their earnings. So how — that on the supply side, yeah.

And then also I would say, we do tons of manual review, and that's also helped us — if we're unsure, we'll put you in QA, a human looks at that internally, our own humans, not external ones. And then we continue to refine based on that. Because for us, yeah, that's kind of like the two things that I would just say that *do* impact experience that fraud can have an impact on. And then we're finding: will that vendor refine their model based on the insights you are giving them, that they are not seeing? And that's something — really terrific.

**Peter:** Well, thank you very much to everyone, I really enjoyed the conversation, it was good fun. So thank you again. I know we did get a chance to answer all the questions — I did get one through email — but if you please do stop the panelists during the break and continue the conversation. So we have a 20-minute break right now, and we'll reconvene in 20 minutes when you hear the bell and the shouts of the town crier.

*[Applause]*

</details>
