# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

Profitable path: tokenB->tokenA->tokenD->tokenC->tokenB
amountIn: 5 (ether)
amountOut: 20.12 (ether)
Final reward: 20.12 (ether)

因為我在實際交易時，在 `swapTokensForExactTokens()` 中將整個 path (`tokenB->tokenA->tokenD->tokenC->tokenB`) 傳入，因此只有一組 swap 的 `amountIn`/`amountOut`。

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

滑點是指 AMM 中交易的預期價格與實際價格之間的差異。

Slippage 指的是交易中預期的價格與實際的價格之間的差距，通常是由市場波動所造成，有時則是因為交易規模、區塊鏈的交易速度等因素所影響。

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

三明治攻擊是利用 gas fee 機制，進行二次交易，把受害者夾在中間，形成三明治的攻擊手法。受害者只能被迫接受巿場價格滑點，攻擊者從中套利。

礦工發現有利可圖的交易後，在該筆交易前後搶先安插其他交易，例如在你要買進之前先買進，價格拉高後倒賣給你；或反過來在你賣出之前先賣出，價格壓低之後再跟你買回。

