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

Slippage (滑價) 是指 AMM 中交易的預期價格與實際價格之間的差異，通常是由市場波動所造成。在 Uniswap V2 中，我們可以透過 `swapExactTokensForTokens()` 中的 `amountOutMin` 或 `swapTokensForExactTokens()` 中的 `amountInMax` 來設定對於滑價的容忍程度，在一定程度上避免了滑價造成的問題。

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

```
if (_totalSupply == 0) {
    liquidity = Math.sqrt(amount0.mul(amount1)).sub(MINIMUM_LIQUIDITY);
    _mint(address(0), MINIMUM_LIQUIDITY); // permanently lock the first MINIMUM_LIQUIDITY tokens
}
```

這個機制是用來防禦 inflation attack，透過銷毀第一個鑄造者 MINIMUM_LIQUIDITY 個代幣，以確保沒有人擁有 LP 代幣的全部供應，避免價格被操縱。

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

```
liquidity = Math.min(amount0.mul(_totalSupply) / _reserve0, amount1.mul(_totalSupply) / _reserve1);
```

這樣的機制鼓勵流動性提供者在增加 token0 與 token1 供應的同時，不會改變 token0 與 token1 的比例。

假設目前池中有 100 個 token0 和 1 個token1，LP token 的供應量為 1。假設這兩個代幣的總價值均為 100 元，因此該池的總價值為 200 元。如果此時有人提供 0 個 token0 和 1 個 token1 (成本 100 元)，並將池中價值提高到 300 元 (將池中價值增加了 50%)。此時若我們選擇以最大比例計算 LP token，則此流動性提供者將可以獲得 1 個 LP token，這意味著他將擁有 50% 的 LP token (因為現在總共有 2 個 LP token)。因此在這個例子中，我們只需存入價值 100 元的資金就可以控制 300 元的流動池的 50%。而這些多餘的流動性是從其他流動性提供者那裡竊取的。

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

三明治攻擊是利用 gas fee 機制，進行二次交易，把受害者夾在中間，形成三明治的攻擊手法。受害者只能被迫接受巿場價格滑點，攻擊者從中套利。

礦工發現有利可圖的交易後，在該筆交易前後搶先安插其他交易，例如：在受害者要買進之前先買進，價格拉高後倒賣給受害者；或反過來在受害者賣出之前先賣出，價格壓低之後再跟受害者買回。

