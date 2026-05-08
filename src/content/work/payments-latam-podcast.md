---
title: "Payments and Delivery in Latin America"
subtitle: "Podcast discussion on the unique challenges of building payment systems across Latin American markets."
publishDate: 2019-08-20 00:00:00
img: /assets/latam-payments.jpg
img_alt: Latin American cityscape representing regional payments landscape
description: |
  Podcast interview with Spreedly discussing the unique challenges of building payment systems across Latin America at PedidosYa.
tags:
  - Podcast
  - Payments
  - Latin America
---

## A conversation with Spreedly

In this episode of Payments Dialog, I sat down with Spreedly's founder and CTO Nathaniel Talbott to discuss the unique challenges of building and scaling payment systems across Latin America while at PedidosYa.

### Topics We Explored

**Latin American Payment Culture** - Why consumer distrust of digital payments remains high, with only 25-30% online payment adoption in markets like Uruguay. The cultural and historical factors that drive preference for cash transactions.

**Multi-Country Operations** - How PedidosYa expanded across nine countries, evolving from food delivery to broader goods delivery including groceries, pharmacy, and alcohol—each with different payment preferences.

**Payment Infrastructure Complexity** - Why we needed 10-11 different payment providers to serve different countries and card types. The challenge of integrating with varying authorization, capture, and refund protocols across the region.

**Fraud Prevention at Scale** - The reality of fraud targeting through small-value test transactions, and why online fraud became more prevalent than cash-on-delivery fraud as we scaled.

**Market Innovation** - How cloud kitchens and logistics optimization changed delivery times, and Uber's unexpected role in normalizing online payments among Latin American consumers.

[Listen to the podcast on Spreedly →](https://www.spreedly.com/blog/payments-dialog-episode-2-payments-and-delivery-in-latin-america-with-mathias-fonseca)

<details>
<summary>View transcript</summary>

> Verbatim transcript adapted from [Spreedly's blog post](https://www.spreedly.com/blog/payments-dialog-episode-2-payments-and-delivery-in-latin-america-with-mathias-fonseca). Light cleanup pass for punctuation and obvious transcription artifacts; substance preserved.

**Nathaniel:** So I'm here with Mathias from PedidosYa, and really excited to talk to him today about Latin America and dig into some of the payments infrastructure, the payments landscape in Latin America.

I'd like to just open up and start out by asking you to tell me a little bit about yourself and your background and PedidosYa, and kind of what PedidosYa does.

**Mathias:** Right. Thank you. First of all, thank you for inviting me. This is great — having the opportunity of sharing what we are doing here. It's something that everybody doesn't know — it's so complicated and so complex, the payments world, the fraud world, even between software developers.

It's like, "I saw you send somebody an amount, I get charged on the card." There's more to it.

I'm a software developer. I lived in Brazil for a while, so my main languages are Spanish and Portuguese. As a software developer, you have to speak English because everything.

I've been working in PedidosYa for five years now. Previously I worked in software factories. PedidosYa is my first product-centered company, and I am very, very proud of what we are doing.

We grew a lot these years. The market is changing and we are doing lots of new things every day. So it's great. Maybe about the company — I think you don't know it, but in the U.S. there are similar companies. PedidosYa focuses mainly on food delivery, but currently we are expanding a little more to make everything come to you. It's like you are on your couch at home on your cellphone and you think of anything, and our objective is to get it to you.

As I said, our main focus is food, so we have a lot of experience in food delivery. But right now we are making groceries, pharmacy, drinks — for example, if you have a party with alcohol or ice, we can deliver it to you.

**Nathaniel:** Awesome. That's really cool. I have a few questions about delivery because it fascinates me, but before we dig into that, I want to ask a little bit about Latin America. Tell me a little bit about how y'all take payments there.

What would you see as major differences between the payments landscape in Latin America versus the US?

**Mathias:** Well, to answer that question, let me tell you a story so I put you in context. I'm not from the capital of Uruguay, I'm from the countryside, and last week when I was talking to Peter about doing this interview, something very funny happened. I went to the countryside to visit my family and I went to a mini supermarket. When I got my things I went to the cash register, gave them my card, and they just said, "no, no, no, we don't take it."

It's like, I'm not trying to pay with Apple Pay — it's a credit card. And I didn't have cash in my wallet. So when I went to the cash register and showed the card, that "new thing"…

"No, no. I don't trust things where I don't get my money right away. I like seeing the bills."

This is a business owner. I said, "wow, I don't have cash." So he said, "I can open like a trust account in the market." He had a notebook, and each sheet had the name of a person, and he kept like a balance.

So you get your debt — I could take the things and go home, and later, another day, maybe next month, I could go to the market and pay. So I think it's a great example of how — this is Uruguay, but I think it happens in Latin America — we are still scared about technology and not seeing things happen in real life.

We have a lot of personal trust and we don't trust digital things. It's like when I say, "yeah, okay, let me transfer, give me your bank account and I can transfer money to you." It's like, "oh no, no, give me money." So it's a continual struggle to convince people to move on.

Right now we are at 30% online payment. That's average in Latin America. In some countries, like Chile for example, you're great. But here in Uruguay it's like 25% or 30%, because of how people are — I'm talking about customers and business owners. The restaurants don't want to accept credit cards, and the customers don't want to put their card on the website.

But I think good things are happening. We are showing people how easy it is to not have cash, to just wait for the delivery guys, take your food, and you don't have to make it. First of all, Uber is helping with that — here it only accepts credit card. Uber is extremely better than taxis here, so you have the customer, you win the customer there, and when you create the account in Uber there's not an option for cash.

So you have to put your credit card, and everybody is like, "oh no, what do we do?" — but they want to use Uber so much that they end up putting the credit card in there. I think that's great for us because it makes the person get to know.

Online payments are the future.

**Nathaniel:** So I guess the question I'd have is: as you're trying to build a delivery company, you end up running smack-dab into all these payments challenges. How much of your job do you feel like is doing delivery logistics, and how much of the job is doing payments at this point?

**Mathias:** Yeah, well, the company PedidosYa belongs to a group of companies called Delivery Hero. They are based in Berlin, and we are like companies all over the world — Asia, Europe, Middle East, Latin America — we are doing similar things.

So we're a big team. We have people specialized in delivery. There are teams I have no idea what they do. For example, there's a team specialized in optimizing the routes for the deliveries — knowing where to have our bikes wait for orders, and where to put them before they deliver, and after they deliver if they go back to the restaurant. There's a lot of logistics that I don't know.

When I started in the company we were like 20, so I was able to answer all the questions that you have.

Right now, counting the delivery guys, the riders as we call them, we are like 2,000 people or more. I'm focused, I'm very focused on payments — the checkout part of the user experience, user journey. But we do a lot. There is a lot of optimization of what the user does.

I mean, one year ago we were just giving a list of restaurants to a user and that's all. We started showing more pictures — you want to see the food that you're gonna eat — so we started sending our own photographers to the restaurants and taking real pictures of the food.

We also added groceries, pharmacy, so the menus that we show had to be different. You know, in a supermarket you have like 500 products — you can't make them a list. So there's people here specialized in things — we were tracking what the user does when he leaves an order unfinished. Why did you do that?

So my job here is to focus on when the user already chose what he's gonna eat. My job is to make the money move. When we started with the payments team we thought our goal was going to be just charging a certain amount of money, but something incredible happened — it was fraud.

Now I changed my email signature to "payments and fraud," because our team right now is very focused on preventing fraud. Trying to realize if the user that's trying to buy is a real person — somebody with the intention of eating that, or reselling it, or trying to test a card.

Unfortunately, we are a pretty good target for people trying to test cards because we have very small amounts. So we have a lot to do. We already did a lot, we have many things pending, but I really love it — it's continuously changing and very dynamic. All our code can change from one day to the other. When a new developer enters the team, I say, "forget everything about requirements." We are always trying things, changing things.

When we find that a fraudster discovered a weakness, we go back to improve it. It's very dynamic.

**Nathaniel:** Since a significant portion of your transactions are cash on delivery — do you have fraud issues there as well? Where does most of the fraud lie? Is most of it in online transactions, or in cash?

**Mathias:** Well, most of the fraud transactions are online, because it's somebody testing a card or maybe testing a lot of cards. The real-life fraud is real, it happens, but it's smaller.

**Nathaniel:** So I'm curious — backing up a little bit to the wider delivery market — was home delivery of food from restaurants and these other goods already a common thing in your markets? In the US we now have services delivering a wide range of things, but when I was growing up it was strictly restaurants, and each restaurant sort of had their own delivery setup.

This new wave of online delivery stuff popped up. What did things look like in Latin America for delivery?

**Mathias:** Well, I have to separate the answer by countries. Here in Uruguay, for example, distances are shorter — we are a very small country and the capital is very small. So everything is like five or ten minutes from you. Restaurant delivery always existed. So many different tastes. Yeah, it always existed. Delivery of other things, here in Uruguay, it's amusing, because when you think about toilet paper it's really easy — you go five minutes and get to a supermarket. But in other countries, in bigger countries like Brazil, Colombia, it's a lot of distance that you have to cover. So delivery of other things always existed.

What we are doing now is trying to create a new way of getting your things. One of the good things about my job is that I'm a user. One interesting thing about restaurant delivery — for example, you mentioned the restaurants have their own fleet of motorbikes. One thing that we are changing is that we provide the logistics. It's like an Uber for food.

We have our bikes and we send them to the restaurant and take the food to houses. Another thing that we are changing — not in Uruguay, it's very common in Asia, for example our partners in Asia — is what we call "cloud kitchens."

The main reason why restaurants exist is that you want to eat. The main reason why the restaurant has tables in it is because you want to eat your food fresh. So you put tables at the restaurant because it's like two meters from you, three meters.

But we are optimizing the logistics so much to get the food to you that we are able to create restaurants that don't exist. They don't have a space for you to go and eat there. That's something that appeared thanks to delivery applications. You have restaurants there — they are extremely small, they are like one table, or maybe two tables and just two chairs — and they are full of delivery guys at the door because they are extremely optimized so that you can get your food.

In the same time that you would receive the food in the restaurant — 10 minutes or maybe less. I think it's going to come to Latin America and the US. These cloud kitchens are like restaurants that don't have a sign. It's only a kitchen — and the chef opens the door and there's a guy waiting on the motorbike, and you get your food in five minutes. It's really useful in Asia because you have millions of people living in a city. If you have the opportunity to squeeze a restaurant in Berlin in a populated area, you have the chance to serve a lot of people.

So maybe a restaurant owner or a chef doesn't have to invest so much, and they have the opportunity to share what they are doing, to share their food. That's, for me, a great idea.

**Nathaniel:** One of the reasons that I get to talk with you is y'all use Spreedly, and I'm particularly curious about — how does the ability to use multiple gateways and interact with multiple payment backends affect your payments flow? Why is that important for the kind of work that you all are doing?

**Mathias:** When we started, around 2015 I think, our first idea was, "well, let's integrate with a payment provider. Let's choose one and go with it." We failed because — for example, PayPal is not an option, there's no penetration, because of what I said about putting your credit card on the internet.

I think the younger people are starting to trust that, but the larger percentage of people don't. In the gateway world, we couldn't find a gateway that covered all of our countries — there are like nine countries. We didn't find a provider that covered all of the cards that we wanted to accept.

Maybe we found one that only accepted Visa, Mastercard, American Express. We wanted to accept local cards, or maybe smaller regional cards, so we ended up with an ecosystem of 10 or 11 providers, depending on the country, depending on the card.

Each provider is better or worse with a type of card, issuer, operation type, credit, debit. In some countries you have different payment methods — for example Chile, it's very common to make a transfer. I think in the U.S. it's called Direct Debit.

In Uruguay, not common. In Brazil they have a lot of options — more options, and more fraud. So we had to adapt to each country. So it became, speaking technically, a mess — because you have to consider all the different kinds of response messages that you get, you have to keep in mind all the possible states that a payment has. For example, some providers allow authorize and capture in two steps, some don't. Some of them allow partial refund.

So it's a jumble. What we are trying to do — that's why we got to know Spreedly — is to unify that. To get the opportunity to sleep at night.

Everything can break down from one minute to the next. What went down? Whose fault is it? Right now it works like 20 actors, because you have all the payment providers — different providers — and in some cases we speak directly to issuers. So my phone is loaded with lots of contacts.

At peak hours — dinner, weekends, or days with rain or an important match — when people are enjoying their meal, I have like two phones on me.

One of our short-term goals is to try to reduce the number of people that we have to contact when something goes wrong, and to reduce or maybe standardize what we say to the customer, because we have a different array of possible errors. Getting to know Spreedly is pretty nice, pretty good for us, because it solves a headache for us and allows us to think of new things.

**Nathaniel:** Well, thank you so much for coming on and chatting with me. I find the different markets fascinating. I think we all wish that we could just pick the one provider when we start out at these things, and then you get into payments — it's endlessly fascinating, just all these different things that people do to exchange money and to issue goods, but it's complicated. It's great to hear some about what's going on in Latin America. So thanks for coming on.

**Mathias:** Thanks to you, it's a pleasure. I love sharing.

</details>
