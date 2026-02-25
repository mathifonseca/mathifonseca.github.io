---
title: "Payments Engineering and Stoicism"
subtitle: "A talk on the mental models that keep payment engineers sane when systems fail at 2am."
publishDate: 2020-03-04 00:00:00
img: /assets/payments-stoicism-thumb.jpg
img_alt: Payments Engineering and Stoicism conference talk thumbnail
description: |
  Conference talk exploring how ancient Stoic philosophy applies to building resilient payment systems in an unpredictable world.
tags:
  - Conference Talk
  - Payments
  - Engineering
---

## How the ancient Greeks were better programmers than you

Regular software engineering trusts that a system, given the same input, will always give the same output. However, when you enter the payments world, anything can happen after you click on that "pay" button.

In this talk, I explore the parallels between Stoic philosophy and payments engineering. The Stoics understood that we cannot control external events—only our responses to them. This wisdom translates directly to building payment systems that must handle:

- **Unpredictable PSP responses** - Timeouts, partial failures, and inconsistent error codes
- **Network unreliability** - The fallacies of distributed computing hit hard in payments
- **Asynchronous reconciliation** - When "success" doesn't mean the money actually moved
- **Fraud and chargebacks** - External actors actively working against your system

The key insight? Build systems that expect failure, not systems that assume success. Design for the chaos, and you'll find peace in production.

[Watch the talk on YouTube →](https://www.youtube.com/watch?v=MGFKVCtzmSU)
