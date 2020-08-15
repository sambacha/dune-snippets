# Dune Snippets

> dune snippets for [duneanalytics.com](https://duneanalytics.com)

## Dune Analytics Documentation 

> source: https://hackmd.io/k71ZUSTxQVKGqOcvR6OXnw



![](https://i.imgur.com/RURn3Pa.png)


## 📑 Documentation for Dune Analytics  

Here are some tips and tricks on how to get started with the data and interface.

Create a user for free at [duneanalytics.com](https://www.duneanalytics.com/).

Submit contracts for decoding at [duneanalytics.com/decode](https://www.duneanalytics.com/decode)

Can't find what you're looking for? Ask our community in our [Telegram channel](https://t.me/dunefriends) or email us at support@duneanalytics.com.



## Dune Analytics TLDR

#### 1. Query human-readable smart contract data with PostgreSQL 🔍
------

![](https://i.imgur.com/Ff16aCN.png)

#### 2. Visualize your findings 📊
------

![](https://i.imgur.com/mYWIFKC.png)

#### 3. Create dashboards and share them with public links 🌎 
------

![](https://i.imgur.com/13W0p7s.png)

#### 4. Explore analysis created by other community members. You can fork any query by the click of a button. 👨‍👩‍👦‍👦
------

![](https://i.imgur.com/8mBfyfl.png)



#### Create a user for free at [Duneanalytics.com](https://www.duneanalytics.com/)

## Table of contents

[TOC]

# 🗂 Data tables

You can currently query from

* [Decoded smart contract data](#decoded-data)
* [Abstractions/table views](#abstractions/table-views)
* [Centralised exchanges trading data](#Centralised-exchanges-trading-data)
* [Raw Ethereum data](#raw-ethereum-data)

The most commonly used tables are

* **Event and call data** for each project where you typically get the action that occured in the smart contract. Simply search for project name to find the relevant tables.
* **Abstractions/view tables** containing abstractions that makes various data very straight forward to query.
* **prices.usd** which gives you USD price of various assets per minute. Typically joined on minute with the event data and multiplied by the on-chain value (trade, transfer etc).
* **erc20.tokens** gives you contract address, symbol and number of decimals for popular tokens. Token value transfers are then divided by `10` to the power of `decimals` from this table.
* **Ethereum transactions** to get ETH transfers. Typically join with event on `ethereum.transactions.hash = evt_tx_hash`.

### Decoded smart contract data

Instead of working with the traces, logs, and receipts, Dune decodes smart contract activity into nice human-readable tables. See the [this section for more info](#🧐-Understanding-data-decoding-in-Dune-Analytics).

### Abstractions/table views

These are the cleanest and easiest to use tables on Dune. We have abstractions for dex trades in the `dex.trades` table.

You can also search for `view` in our table list to find all the various views.  

Together with various teams and community members we've created table views that make the blockchain data even easier to work with. This typically entails removing decimals for ETH and token transfers, adding human readable symbols, joining relevant tables together, adding USD value of events and more.

You can always see the underlying tables derived directly from the blockchain if you need more detials or are curious about how the views are created: [check out our Github](https://github.com/duneanalytics/abstractions), you can even do a pull request to create your own abstarctions. 


#### Raw Ethereum data
 
* Blocks
* Logs
* Transactions
* Receipts
* Traces

You probably won't use this too much when doing analysis with Dune (see [decoded data](#decoded-data)), but it's always nice to have just in case. 

You can [click here](https://ethereum.stackexchange.com/questions/268/ethereum-block-architecture)  to learn more about Ethereum's data structure, but again it's not really needed for using Dune.

### Centralised exchanges trading data 

Token volume is great, but more often than not you want to know the USD value of smart contract activity.

You can easily get and join that information with onchain data using the data we pull from the coincap API. See how to use it below.

* prices.usd
    * contract_address
    * price
    * minute
    * symbol (ticker)

Price is the volume-weighted price based on real-time market data every minute, translated to USD.

The data is fetched from this [Coincap API](https://docs.coincap.io/?0=o&1=n&2=b&3=o&4=a&5=r&6=d&7=i&8=n&9=g&10=c&11=o&12=m&13=p&14=l&15=e&16=t&17=e&version=latest#61e708a8-8876-4fb2-a418-86f12f308978).


# 👨‍🏫 Tips for querying the data

You can interact with the [data tables](#Data-tables) through our interface at [duneanalytics.com](https://www.duneanalytics.com/).

To create a new query you simply click Create -> Query

![](https://i.imgur.com/FVLbPef.png)

On your left you can select which database you want to use in the dropdown list and then see the data tables in the window. Just search for the project you are interested in working with.

### Use view abstractions and tables

The easiest way to do great analysis with Dune Analytics is to use the tables that are named `namespace.view_` or abstraction tables like `dex.trades`. All the view tables are cleaned and contains data and metadata (like human readable token symbols) that make them very straight forward to query. 

### Using Inline Ethereum addresses

In Dune Ethereum addresses are stored as postgres bytearrays which are encoded with the `\x` prefix. This differs from the customary `0x` prefix. If you'd like to use an inline address, say to filter for a given token, you would do
```sql
WHERE token = '\x6b175474e89094c44da98b954eedeac495271d0f'
```
which is simply short for 
``` sql
WHERE token = '\x6b175474e89094c44da98b954eedeac495271d0f'::bytea
```

### Quote camel case column and table names

Column and table names in Dune are often camel case. When you query you therefore need to quote them.

```SQL
SELECT “columnName”
FROM projectname.”contratName_evt_eventName”
LIMIT 10
```

Project names are always lowercase.

When you want to filter for a specific value you use single quotes:

```SQL
SELECT “columnName”
FROM projectname.”contratName_evt_eventName”
WHERE contract_address = '\x6B175474E89094C44Da98b954EedeAC495271d0F'
LIMIT 10
```

### Remove decimals

Ether transfers and most ERC-20 tokens have 18 decimal places. To get a more human readable number you need to remove all the decimals. The table `erc20.tokens` gives you contract address, symbol and number of decimals for popular tokens. Token value transfers are then divided by 10 to the power of decimals from this table:

`transfer_value / 10^erc20.tokens.decimals`

### Use `date_trunc` to get time

We've added `evt_block_time` to the event tables for your convenience. A neat way to use it is with the `date_trunc` function like this 

```SQL
SELECT date_trunc('week', evt_block_time) AS time
```
Here you can use minute, day, week, month.

### How to get USD price

To get the USD volume of onchain activity you typically want to join the smart contract event you are looking at with the usd price and join on minute. Also make sure that asset matches asset.
 
``` SQL
LEFT JOIN prices.usd p 
ON p.minute = date_trunc('minute', evt_block_time)
AND event."asset" = p.contract_address
```

Then you can simply multiply the value or amount from the smart contract event with the usd price in your `SELECT` statement: `* p.price`. 

### Token symbols

You often want to group your results by token address. For instance you want to see volume on a DEX grouped by token. However, a big list of token addresses are abstract and hard to digest.

Therefore you often want to use the token symbol instead. Simply join the table `erc20.tokens` with your event table where asset = token address. You then select symbol in your select statement instead of token address.

**NB** The `erc20.tokens` table cointains a selection of popular tokens. If you are working with more obscure tokens you should be careful with joining with this table because tokens that are not in the coincap table might be excluded from your results. 


# 🧐 Understanding data decoding in Dune Analytics

This section contains a quick primer on how you can explore what decoded data we have and the methods we use to decode the data. 

In Dune, there are tables for each event and function defined in the smart contract ABI. Subsequently, every event or function call on that contract is decoded and inserted as rows into these tables.

The tables are named accordingly

events:`projectname."contractName_evt_eventName"` 

function calls: `projectname."contractName_call_eventName"` 

As an example, decoded data for the `AddLiquidity`-event and `addLiquidity`-function of the uniswap exchange contract are found in tables

`uniswap."Exchange_evt_AddLiquidity"` and `uniswap."Exchange_call_addLiquidity"`.

Using the event tables is usually sufficient, but in some cases you will want to use the `call` tables. For instance Maker DAO which don't give you too many events you can use tables like `maker.SaiTub_call_draw`.

## What contracts have decoded data?

### Decoded data

By querying `ethereum.contracts`, you can get an overview over which contracts are tracked by the Dune backend. The columns are

```sql
namespace -- Project/product name
name -- Contract name
ABI -- The ABI that will populate the relevant tables
address -- The contract address
dynamic -- True if all contracts with the same bytecode are decoded automatically
bytecode -- The bytecode for the decoded contract
```

### Abstractions and views 

On top of the decoded tables we have a growing number of views that make it even easier to work witht the data. 

Views are named `namespace.view_event` for instance. In general you can search for `view` in the table list to find the views we have. 

### A few handy queries to explore decoded tables

**See all projects we have decoded data for** 

```sql
SELECT DISTINCT namespace FROM ethereum."contracts"; 
```

**Do we have decoded data for a specific contract?**

```sql
SELECT * FROM ethereum."contracts"
WHERE address = '\xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2';
```

**Contracts that are "interface"-decoded**

```sql
SELECT * FROM ethereum."contracts" WHERE address IS NULL;
```

If you are working with a an event or call table directly you can see if there are several instances of that contract with  

```sql
SELECT DISTINCT contract_address FROM projectname."contractName_evt_eventName"; 
```



## Scalable decoding across contracts

Many dApps have numerous smart contracts that are more or less similar, we have two main ways of handling this in a scalable way: 

### Contracts with the same bytecode

Dune can dynamically add  contracts to track by comparing the bytecode of deployed contracts to known bytecodes. If a known contract is "dynamic", events and calls to a newly deployed contract with matching bytecode will find it's way into the same tables as were defined by the base contract. Essentially this covers all factory-pattern contract architectures. As a result, `SELECT`-ing from a single table might yield data from multipole contracts. In decoded tables, the column `contract_address` tells you which smart contract the event or call is on. If you want to look at only a single contract you filter may filter by its address. 

For example:

```sql
SELECT DISTINCT contract_address FROM uniswap."Exchange_evt_TokenPurchase";
```

Will give you all the unique Uniswap exchanges with a Token Purchase event. 

### Interfaces

When we're interested in a subset of events fired regardless of the origin contract, Dune uses interface-decoding. Notable examples include erc20 and erc721 transfer events. This method is reserved for special cases.

## How Dune handles Proxy contracts

Sometimes users interact with dApps through proxy contracts. The proxy contract throws the event, but there's an underlying contract that contains and performs the action. In those cases, we apply the ABI of the proxied contract (sometimes called "master copy") to the proxy contract address. We also usually apply the name of the proxied contract to the relevant table. 

# 📬 Get any smart contract decoded

#### We have decoded data for the most popular smart contract projects. Head to duneanalytics.com/decode if you have a request for decoding of data.

# 👩‍🏭 Change log

#### [March 2020](https://hackmd.io/YOP3YIgaRAejTPE190sOjw?view#March-2020) - block_time denormalization, traces.success and more
#### [January 2020](https://hackmd.io/YOP3YIgaRAejTPE190sOjw?view) - ERC20 transfer table, Fallback decoding and more
#### [October 2019](https://hackmd.io/YOP3YIgaRAejTPE190sOjw?view#October-2019) - New data structure

# 👉 Some sample queries

## Growth rate

Assuming you have a query with a count of some event grouped by time (month for instance) you can add this snippet to you `select` statement to get growth rate.

```SQL
(count(distinct event) - lag(count(distinct event), 1)
over (order by date_trunc('month', evt_block_time))) / lag(count(distinct action), 1)
over (order by date_trunc('month', evt_block_time)) as "Growth rate"
```

Multiply the number by 100 to get percentage.

## Users and amount over a trailing period

```sql
SELECT  date_trunc('day', evt_block_time),
        COUNT (DISTINCT buyer),
        SUM(eth_bought / 1e18)
FROM uniswap."Exchange_evt_EthPurchase" p
WHERE evt_block_time > now() - interval '7 days'
GROUP BY 1
ORDER BY 1;
```

## Circulating supply over time of a token with mint/burn functions

```SQL
SELECT
week,
SUM(transfer) over (order by week)
FROM 
 (
    SELECT
    date_trunc('week', evt_block_time) as week,
    sum(amount/1e18) as transfer
    FROM ptokens."pBTC_evt_Minted" tr
    GROUP BY 1
UNION
    SELECT
    date_trunc('week', evt_block_time) as week,
    sum(-amount/1e18) as transfer
    FROM ptokens."pBTC_evt_Burned" tr
    GROUP BY 1
) as net;
```

## Circulating supply over time with mint/burn from `0x000...` address

```SQL

SELECT
week,
SUM(transfer) over (order by week)
FROM 
 (
    SELECT
    date_trunc('week', evt_block_time) as week,
    sum(value/1e8) as transfer --Divide by relevant decimal number
    FROM erc20."ERC20_evt_Transfer"
    WHERE contract_address = '\x2260fac5e5542a773aa44fbcfedf7c193bc2c599' -- token contract address
    AND "from" = '\x0000000000000000000000000000000000000000'
    GROUP BY 1
UNION
    SELECT
    date_trunc('week', evt_block_time) as week,
    sum(-value/1e8) as transfer --Divide by relevant decimal number
    FROM erc20."ERC20_evt_Transfer"
    WHERE contract_address = '\x2260fac5e5542a773aa44fbcfedf7c193bc2c599' -- token contract address
    AND "to" = '\x0000000000000000000000000000000000000000'
    GROUP BY 1
) as net;


```

## USD value of token utilised for an event

```sql
SELECT
date_trunc('week', evt_block_time),
SUM(amount/1e18 * p.price) AS staked
FROM numerai."SimpleGriefing_evt_StakeAdded" s --Replace with relevant event
LEFT JOIN prices.usd p ON p.minute = date_trunc('minute', evt_block_time)
WHERE p.symbol = 'NMR' --Replace with relevant token
GROUP BY 1;
```



## USD trading volume per token over time

```sql
SELECT    price.symbol,
          date_trunc('week', evt_block_time) AS time,
          SUM(["FilledAmount"] /10^(erc.decimals) * price.price) AS usd_value
   FROM [table].["fill_event"] filled
   LEFT JOIN prices.usd price ON date_trunc('minute', evt_block_time) = price.minute AND [tokenAddress] = price.contract_address
   LEFT JOIN erc20.tokens erc ON erc.contract_address = "takerAsset"
    WHERE evt_block_time < date_trunc('week', current_date)::date
   GROUP BY 1,
            2;
```



## 🤕 Known issues

### Function overloading

We have a known issue with *function overloading*. There are a few cases where smart contract developers use function overloading, i.e. specify two functions with the same name but different parameters. In these cases, we will currently only have _one_ of the implementations in our database. We’re working on a fix for this. One known case is the two approve implementations in the SAI contract.


