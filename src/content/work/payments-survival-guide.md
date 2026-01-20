---
title: "A Survival Guide for Payments"
publishDate: 2019-11-01 00:00:00
img: /assets/survival-guide.jpg
img_alt: Analytics dashboard representing payments monitoring and observability
description: |
  A comprehensive collection of advice, stories, and learnings about life as a payments engineer, adapted from my PAYMENTSfn 2019 talk.
tags:
  - Article
  - Payments
  - Engineering
---

Why are PSP (payment service provider) integrations so painful? Why is it so hard to estimate? Isn't it just calling two API endpoints?

After years of tripping into the same stones multiple times, this is an attempt to collect an assorted list of advice, stories, and learnings about our life as payments engineers.

*This post is adapted from my 2019 talk at PAYMENTSfn.*

---

## Process & Team

### Change the methodology
PSP integrations are susceptible to unpredictable timelines. Your team will benefit from a workflow that can adapt to blockers and switch contexts without the risk of losing track of the work. I've found Kanban to be a good fit, but make sure to choose something that works for your team.

### Split the team
It's a mistake to put all of your development team on one integration as it puts their velocity at risk if there's a sudden blocker. At the same time, having one person per integration is also harmful as it creates a knowledge silo. Splitting the team by pairs helps share knowledge and encourages communication.

### What release cycle?
Remember those unpredictable timelines? PSPs don't care about your deadlines, so you can pretty much forget about strict deadlines. They could go into some form of maintenance mode, or a key feature could suddenly stop working as intended.

---

## Planning & Requirements

### Chargebacks and webhooks are a thing
Both chargeback and webhook handling often get overlooked. Don't wait until the last minute, as these are important to handle correctly without rushing.

### Get the bigger picture
Be careful about buying into a PSP because they have a nice API or documentation. It's important to understand the perspective of your business to drive these decisions. The PSP engineers love may be too expensive or unavailable in a country that's critical to stakeholders.

### Don't sign first; ask first
Get involved in business decisions so you can help catch any red flags for engineering.

### You are also a customer
Design a payments system that you'd want to use. Do you want to fill out 40 fields to purchase a pizza? I don't think so.

### PSPs also have a product
Each PSP will try to sell you on their various products and integrations. Choose wisely as you don't want to become so locked in that change becomes rigid.

---

## Communication

### Keep product calm
Communicate the differences between PSPs to your product team to help make sense of timeline differences.

### Complain with facts
If something is wrong with the PSP, approach them with facts and data from the start to demonstrate the problem. It's far too easy to be dismissed because it's working on their end.

### Weekly calls
During integration and after, have weekly/monthly calls with your PSP. Have them involved in the process of your integration. Be active and get feedback by showing your integration.

---

## Documentation

### Feature checklist
Write down the core parts of your integration, so you don't forget what features are required for integrations or changes.

### Diagrams, glossaries, and docs
Don't rely on memory. Leverage your documentation even if the PSP provides it, so your understanding is captured.

---

## Support & Escalation

### Find support
During the initial integration, get all the support information you can ahead of time. Emails, phone numbers, addresses, whatever it takes to have a point of contact when something goes wrong.

### Find allies
It's great to find a developer contact so you can approach them with concrete examples when things aren't working correctly.

### Define escalations
Make sure you know who is responsible for escalation when something goes wrong. Don't leave it to guesswork.

### Big red button
When your payments system is broken, it's critical to have a way to shut down or re-route portions of payments quickly. This will come in useful when you know something is wrong and need a way to prevent customer impact.

### Does it really work?
Have the PSP give you a demo of how something works if you are experiencing issues. This helps straighten out the "it's working on my machine" scenarios.

### Don't idealize others
This is general life advice. Don't idealize the systems or people and recognize they can be just as messy and chaotic.

---

## Testing & Infrastructure

### Test in production
You'll need to test in production and have a strategy. Not every PSP will have a reliable sandbox mode.

### Feature flags
Make use of feature flags to release small portions that can be tested in production. This is great for testing before an official release.

### Fake PSP for load testing
The chances are that everything is going to be ideal when testing in development. So how do you create the scenarios of timeouts or crashes? Create a fake PSP so you can introduce errors and delay for real-life load testing.

### Split infrastructure
Don't let one PSP going down crash your entire payments system. Of course, do this within reason, so your costs don't skyrocket.

---

## Monitoring & Observability

### Define dynamic alerts
Don't cry wolf when one payment fails. And don't assume a 100% charge success rate means nothing is wrong. You need dynamic monitoring for anomalies.

### Dashboards for dummies
Do yourself a favor and make sure there's a dashboard that anyone in the organization can find to see the status of payments. This way, you won't get calls in the middle of the night if someone thinks your system is down.

### Know your timeouts
Keep track of the different timeouts between each PSP so you don't reject calls due to improper timeout handling.

### try/catch/finally { print }
When things go wrong, print! You want logs, especially when the error is catastrophic. Don't let fatal errors go unnoticed.

---

## Integration Strategy

### Ask stupid questions
Don't assume and ask all the questions. Each PSP behaves differently, and it's better to find out nuances sooner.

### Integrate many
Having one PSP is risky as you won't be able to handle an outage. If you only have one PSP, avoid basing your entire payment system on its interface.

### Aggregate integrations
Identify the common parts so that code can be made adaptable.

### Make the code speak
It should be straightforward for anyone to see how data maps exist between integrations instead of searching through the codebase to figure it out.

### Reduce client-side code
Try to keep as much in the server to avoid needing to update the client and server whenever a PSP integration requires a change.

### Design for extension
PSPs are starting to become PSPs of PSPs. Prepare yourself for multiple layers by designing for extension.

---

## Defensive Coding

### Defensive programming
Everything can fail, so code accordingly.

### Null, Empty, "Null", "dummy"
Each PSP will handle null or empty params differently. Make sure you account for these.

### Size matters
You need to know limits in your fields to avoid simple mistakes that can break an integration.

### yyyy-MM-dd hh:mm:ss UTC
Prepare for all possible formats so you can convert them safely. This happens to be my favorite format for dates because you can sort them alphabetically.

### Numbers and currencies
Is it minor units? Cents? Is it a double? A float? A string? Does it need rounding? You need to make sure you always know.

### Optional is mandatory
Assume everything is mandatory so you can quickly adapt. It's much easier to over send data than to collect additional data.

### Billing and shipping address
Yes, they are different, and it's important to know what your PSP requires. If you don't collect shipping addresses and your PSP requires it, what value will you send? Can it be blank?

### First, middle, and last name
Separate or together? How do you split them? Each PSP has different fields.

---

## Technical Choices

### Give SOAP a REST
REST is great, but it isn't all magic, so don't throw out SOAP. It's not better, but different.

### SDKs are not that good
Only use them if they are adding value. Otherwise, you'd need to keep up with version changes that may or may not break your integration.

### Exceptions are exceptional
Don't raise exceptions unless it's exceptional. Failed payments aren't exceptional. Handle errors correctly.

### Detailed errors to avoid questions
The more clarity you can provide to a customer, the fewer amount of questions you'll receive. Be sure not to reveal too much information.

### Validate before the PSP
Don't send information you can check beforehand.

### Async is your friend
It's great to take out parts of the flow to be async, but be mindful of the complexity tradeoff.

### Conditionals are configs
Code that says something along the lines of "if this card is this scheme for this country, then do…." should be a configuration. Convert the code, make it generic, and then consolidate it.

### Implement GETs
Ensure you can fetch the tokens, payments, etc., even if you don't readily need them, so you have access in a hurry if something goes wrong. If there's a timeout and you want to check if the payment is made, do you have the get operation to do that?

---

## Domain Knowledge

### Care about statement descriptors
Helpful for chargebacks and debugging.

### Schemes, brands, types, etc
Know and use the differences between them all.

### Credit, void, cancel, refund
They all behave differently, and sometimes a PSP comes up with their own terminology. Spend time understanding their definitions. Map what they mean and what your understanding is within your system.

---

## Data Management

### Keep all data
Be secure and compliant, but keep as much data as you can.

### Log everything
Logs are critical but ensure you remove PCI information.

### No back offices
Avoid changes made from within the PSP. Refunding a transaction from the PSP dashboard is likely to result in your data becoming inconsistent.

### No updates, just inserts
One line per update. A payment has a life-cycle, and you'll want to know how it changed.

### Store queryable JSON
Store responses and requests in case you need that field someday. This is particularly great if you find that you need to use data from a field that wasn't necessary at the time. Keep in mind that JSON queries can be slow, and avoid using them in critical paths.

### IDs everywhere
Send your IDs to the PSP and keep their IDs to make reconciliation easier.

### Card tokens are a list
Allow multiple tokens per card so you can switch PSPs without asking the user to re-enter their information.
