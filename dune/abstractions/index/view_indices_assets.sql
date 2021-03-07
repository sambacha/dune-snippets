CREATE OR REPLACE VIEW index.view_indices_assets (Index, project, asset, asset_address) AS VALUES
('ASSY'     ::text, 'PowerPool' ::text,    'AAVE'	    ::text,   '\x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9'::bytea),
('ASSY'     ::text, 'PowerPool' ::text,    'SNX'	    ::text,   '\xc011a73ee8576fb46f5e1c5751ca3b9fe0af2a6f'::bytea),
('ASSY'     ::text, 'PowerPool' ::text,    'SUSHI'	    ::text,   '\x6b3595068778dd592e39a122f4f5a5cf09c90fe2'::bytea),
('ASSY'     ::text, 'PowerPool' ::text,    'YFI'	    ::text,   '\x0bc529c00c6401aef6d220be8c6ea1667f6ad93e'::bytea),
('BCP'      ::text, 'pieDAO'    ::text,    'WBTC'	    ::text,   '\x2260fac5e5542a773aa44fbcfedf7c193bc2c599'::bytea),
('BCP'      ::text, 'pieDAO'    ::text,    'WETH'	    ::text,   '\xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'::bytea),
('BCP'      ::text, 'pieDAO'    ::text,    'DEFI++'     ::text,   '\x8d1ce361eb68e9e05573443c407d4a3bed23b033'::bytea),
('BTC++'    ::text, 'pieDAO'    ::text,    'WBTC'	    ::text,   '\x2260fac5e5542a773aa44fbcfedf7c193bc2c599'::bytea),
('BTC++'    ::text, 'pieDAO'    ::text,    'imBTC'	    ::text,   '\x3212b29e33587a00fb1c83346f5dbfa69a458923'::bytea),
('BTC++'    ::text, 'pieDAO'    ::text,    'pBTC'	    ::text,   '\x5228a22e72ccc52d415ecfd199f99d0665e7733b'::bytea),
('BTC++'    ::text, 'pieDAO'    ::text,    'sBTC'	    ::text,   '\xfe18be6b3bd88a2d2a7f928d00292e7a9963cfc6'::bytea),
('CC10'     ::text, 'Indexed'   ::text,    'COMP'	    ::text,   '\xc00e94cb662c3520282e6f5717214004a7f26888'::bytea),
('CC10'     ::text, 'Indexed'   ::text,    'UMA'	    ::text,   '\x04fa0d235c4abf4bcf4787af4cf447de572ef828'::bytea),
('CC10'     ::text, 'Indexed'   ::text,    'YFI'	    ::text,   '\x0bc529c00c6401aef6d220be8c6ea1667f6ad93e'::bytea),
('CC10'     ::text, 'Indexed'   ::text,    'CRV'	    ::text,   '\xd533a949740bb3306d119cc777fa900ba034cd52'::bytea),
('CC10'     ::text, 'Indexed'   ::text,    'LINK'	    ::text,   '\x514910771af9ca656af840dff83e8264ecf986ca'::bytea),
('CC10'     ::text, 'Indexed'   ::text,    'SNX'	    ::text,   '\xc011a73ee8576fb46f5e1c5751ca3b9fe0af2a6f'::bytea),
('CC10'     ::text, 'Indexed'   ::text,    'MKR'	    ::text,   '\x9f8f72aa9304c8b593d555f12ef6589cc3a579a2'::bytea),
('CC10'     ::text, 'Indexed'   ::text,    'AAVE'	    ::text,   '\x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9'::bytea),
('CC10'     ::text, 'Indexed'   ::text,    'UNI'	    ::text,   '\x1f9840a85d5af5bf1d1762f925bdaddc4201f984'::bytea),
('CC10'     ::text, 'Indexed'   ::text,    'OMG'	    ::text,   '\xd26114cd6ee289accf82350c8d8487fedb8a0c07'::bytea),
('CGI'      ::text, 'IndexCoop' ::text,    'WETH'	    ::text,   '\xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'::bytea),
('CGI'      ::text, 'IndexCoop' ::text,    'WBTC'	    ::text,   '\x2260fac5e5542a773aa44fbcfedf7c193bc2c599'::bytea),
('CGI'      ::text, 'IndexCoop' ::text,    'wDGLD'	    ::text,   '\x123151402076fc819B7564510989e475c9cD93CA'::bytea),
('DEFI++'   ::text, 'pieDAO'    ::text,    'DEFI+S'     ::text,   '\xad6a626ae2b43dcb1b39430ce496d2fa0365ba9c'::bytea),
('DEFI++'   ::text, 'pieDAO'    ::text,    'DEFI+L'     ::text,   '\x78f225869c08d478c34e5f645d07a87d3fe8eb78'::bytea),
('DEFI+L'   ::text, 'pieDAO'    ::text,    'COMP'	    ::text,   '\xc00e94cb662c3520282e6f5717214004a7f26888'::bytea),
('DEFI+L'   ::text, 'pieDAO'    ::text,    'MKR'	    ::text,   '\x9f8f72aa9304c8b593d555f12ef6589cc3a579a2'::bytea),
('DEFI+L'   ::text, 'pieDAO'    ::text,    'YFI'	    ::text,   '\x0bc529c00c6401aef6d220be8c6ea1667f6ad93e'::bytea),
('DEFI+L'   ::text, 'pieDAO'    ::text,    'AAVE'	    ::text,   '\x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9'::bytea),
('DEFI+L'   ::text, 'pieDAO'    ::text,    'UNI'	    ::text,   '\x1f9840a85d5af5bf1d1762f925bdaddc4201f984'::bytea),
('DEFI+L'   ::text, 'pieDAO'    ::text,    'LINK'	    ::text,   '\x514910771af9ca656af840dff83e8264ecf986ca'::bytea),
('DEFI+L'   ::text, 'pieDAO'    ::text,    'SNX'	    ::text,   '\xc011a73ee8576fb46f5e1c5751ca3b9fe0af2a6f'::bytea),
('DEFI+S'   ::text, 'pieDAO'    ::text,    'UMA'	    ::text,   '\x04fa0d235c4abf4bcf4787af4cf447de572ef828'::bytea),
('DEFI+S'   ::text, 'pieDAO'    ::text,    'REN'	    ::text,   '\x408e41876cccdc0f92210600ef50372656052a38'::bytea),
('DEFI+S'   ::text, 'pieDAO'    ::text,    'MLN'	    ::text,   '\xec67005c4e498ec7f55e092bd1d35cbc47c91892'::bytea),
('DEFI+S'   ::text, 'pieDAO'    ::text,    'LRC'	    ::text,   '\xbbbbca6a901c926f240b89eacb641d8aec7aeafd'::bytea),
('DEFI+S'   ::text, 'pieDAO'    ::text,    'PNT'	    ::text,   '\x89ab32156e46f46d02ade3fecbe5fc4243b9aaed'::bytea),
('DEFI+S'   ::text, 'pieDAO'    ::text,    'BAL'	    ::text,   '\xba100000625a3754423978a60c9317c58a424e3d'::bytea),
('DEFI5'    ::text, 'Indexed'   ::text,    'AAVE'	    ::text,   '\x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9'::bytea),
('DEFI5'    ::text, 'Indexed'   ::text,    'UNI'	    ::text,   '\x1f9840a85d5af5bf1d1762f925bdaddc4201f984'::bytea),
('DEFI5'    ::text, 'Indexed'   ::text,    'SNX'	    ::text,   '\xc011a73ee8576fb46f5e1c5751ca3b9fe0af2a6f'::bytea),
('DEFI5'    ::text, 'Indexed'   ::text,    'COMP'	    ::text,   '\xc00e94cb662c3520282e6f5717214004a7f26888'::bytea),
('DEFI5'    ::text, 'Indexed'   ::text,    'CRV'	    ::text,   '\xd533a949740bb3306d119cc777fa900ba034cd52'::bytea),
('DEGEN'    ::text, 'Indexed'   ::text,    'CRV'	    ::text,   '\xd533a949740bb3306d119cc777fa900ba034cd52'::bytea),
('DEGEN'    ::text, 'Indexed'   ::text,    'RUNE'	    ::text,   '\x3155ba85d5f96b2d030a4966af206230e46849cb'::bytea),
('DEGEN'    ::text, 'Indexed'   ::text,    'REN'	    ::text,   '\x408e41876cccdc0f92210600ef50372656052a38'::bytea),
('DEGEN'    ::text, 'Indexed'   ::text,    'RSR'	    ::text,   '\x8762db106b2c2a0bccb3a80d1ed41273552616e8'::bytea),
('DEGEN'    ::text, 'Indexed'   ::text,    '1INCH'	    ::text,   '\x111111111117dC0aa78b770fA6A738034120C302'::bytea),
('DEGEN'    ::text, 'Indexed'   ::text,    'OCEAN'	    ::text,   '\x967da4048cD07aB37855c090aAF366e4ce1b9F48'::bytea),
('DEGEN'    ::text, 'Indexed'   ::text,    'ALPHA'	    ::text,   '\xa1faa113cbe53436df28ff0aee54275c13b40975'::bytea),
('DEGEN'    ::text, 'Indexed'   ::text,    'BADGER'	    ::text,   '\x3472A5A71965499acd81997a54BBA8D852C6E53d'::bytea),
('DEGEN'    ::text, 'Indexed'   ::text,    'POLS'	    ::text,   '\x83e6f1E41cdd28eAcEB20Cb649155049Fac3D5Aa'::bytea),
('DEGEN'    ::text, 'Indexed'   ::text,    'MIR'	    ::text,   '\x09a3ecafa817268f77be1283176b946c4ff2e608'::bytea),
('DPI'      ::text, 'IndexCoop' ::text,    'LEND'	    ::text,   '\x80fb784b7ed66730e8b1dbd9820afd29931aab03'::bytea),
('DPI'      ::text, 'IndexCoop' ::text,    'LRC'	    ::text,   '\xbbbbca6a901c926f240b89eacb641d8aec7aeafd'::bytea),
('DPI'      ::text, 'IndexCoop' ::text,    'BAL'	    ::text,   '\xba100000625a3754423978a60c9317c58a424e3d'::bytea),
('DPI'      ::text, 'IndexCoop' ::text,    'MTA'	    ::text,   '\xa3bed4e1c75d00fa6f4e5e6922db7261b5e9acd2'::bytea),
('DPI'      ::text, 'IndexCoop' ::text,    'REN'	    ::text,   '\x408e41876cccdc0f92210600ef50372656052a38'::bytea),
('DPI'      ::text, 'IndexCoop' ::text,    'YFI'	    ::text,   '\x0bc529c00c6401aef6d220be8c6ea1667f6ad93e'::bytea),
('DPI'      ::text, 'IndexCoop' ::text,    'COMP'	    ::text,   '\xc00e94cb662c3520282e6f5717214004a7f26888'::bytea),
('DPI'      ::text, 'IndexCoop' ::text,    'REPv2'	    ::text,   '\x221657776846890989a759ba2973e427dff5c9bb'::bytea),
('DPI'      ::text, 'IndexCoop' ::text,    'SNX'	    ::text,   '\xc011a73ee8576fb46f5e1c5751ca3b9fe0af2a6f'::bytea),
('DPI'      ::text, 'IndexCoop' ::text,    'KNC'	    ::text,   '\xdd974d5c2e2928dea5f71b9825b8b646686bd200'::bytea),
('DPI'      ::text, 'IndexCoop' ::text,    'AAVE'	    ::text,   '\x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9'::bytea),
('DPI'      ::text, 'IndexCoop' ::text,    'UNI'	    ::text,   '\x1f9840a85d5af5bf1d1762f925bdaddc4201f984'::bytea),
('DPI'      ::text, 'IndexCoop' ::text,    'MKR'	    ::text,   '\x9f8f72aa9304c8b593d555f12ef6589cc3a579a2'::bytea),
('DPI'      ::text, 'IndexCoop' ::text,    'SUSHI'	    ::text,   '\x6b3595068778dd592e39a122f4f5a5cf09c90fe2'::bytea),
('ORCL5'    ::text, 'Indexed'   ::text,    'DIA'	    ::text,   '\x84ca8bc7997272c7cfb4d0cd3d55cd942b3c9419'::bytea),
('ORCL5'    ::text, 'Indexed'   ::text,    'ORAI'	    ::text,   '\x4c11249814f11b9346808179cf06e71ac328c1b5'::bytea),
('ORCL5'    ::text, 'Indexed'   ::text,    'UMA'	    ::text,   '\x04fa0d235c4abf4bcf4787af4cf447de572ef828'::bytea),
('ORCL5'    ::text, 'Indexed'   ::text,    'LINK'	    ::text,   '\x514910771af9ca656af840dff83e8264ecf986ca'::bytea),
('ORCL5'    ::text, 'Indexed'   ::text,    'BAND'	    ::text,   '\xba11d00c5f74255f56a5e366f4f77f5a186d7f55'::bytea),
('PIPT'     ::text, 'PowerPool' ::text,    'SNX'	    ::text,   '\xc011a73ee8576fb46f5e1c5751ca3b9fe0af2a6f'::bytea),
('PIPT'     ::text, 'PowerPool' ::text,    'YFI'	    ::text,   '\x0bc529c00c6401aef6d220be8c6ea1667f6ad93e'::bytea),
('PIPT'     ::text, 'PowerPool' ::text,    'CVP'	    ::text,   '\x38e4adb44ef08f22f5b5b76a8f0c2d0dcbe7dca1'::bytea),
('PIPT'     ::text, 'PowerPool' ::text,    'COMP'	    ::text,   '\xc00e94cb662c3520282e6f5717214004a7f26888'::bytea),
('PIPT'     ::text, 'PowerPool' ::text,    'AAVE'	    ::text,   '\x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9'::bytea),
('PIPT'     ::text, 'PowerPool' ::text,    'MKR'	    ::text,   '\x9f8f72aa9304c8b593d555f12ef6589cc3a579a2'::bytea),
('PIPT'     ::text, 'PowerPool' ::text,    'UNI'	    ::text,   '\x1f9840a85d5af5bf1d1762f925bdaddc4201f984'::bytea),
('USD++'    ::text, 'pieDAO'    ::text,    'sUSD'	    ::text,   '\x57ab1ec28d129707052df4df418d58a2d46d5f51'::bytea),
('USD++'    ::text, 'pieDAO'    ::text,    'TUSD'	    ::text,   '\x0000000000085d4780b73119b644ae5ecd22b376'::bytea),
('USD++'    ::text, 'pieDAO'    ::text,    'DAI'	    ::text,   '\x6b175474e89094c44da98b954eedeac495271d0f'::bytea),
('USD++'    ::text, 'pieDAO'    ::text,    'USDC'	    ::text,   '\xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'::bytea),
('YETI'     ::text, 'PowerPool' ::text,    'PICKLE'     ::text,   '\x429881672b9ae42b8eba0e26cd9c73711b891ca5'::bytea),
('YETI'     ::text, 'PowerPool' ::text,    'KP3R'	    ::text,   '\x1ceb5cb57c4d4e2b2433641b95dd330a33185a44'::bytea),
('YETI'     ::text, 'PowerPool' ::text,    'COVER'	    ::text,   '\x4688a8b1f292fdab17e9a90c8bc379dc1dbd8713'::bytea),
('YETI'     ::text, 'PowerPool' ::text,    'SUSHI'	    ::text,   '\x6b3595068778dd592e39a122f4f5a5cf09c90fe2'::bytea),
('YETI'     ::text, 'PowerPool' ::text,    'YFI'	    ::text,   '\x0bc529c00c6401aef6d220be8c6ea1667f6ad93e'::bytea),
('YETI'     ::text, 'PowerPool' ::text,    'AKRO'	    ::text,   '\x8ab7404063ec4dbcfd4598215992dc3f8ec853d7'::bytea),
('YETI'     ::text, 'PowerPool' ::text,    'CREAM'	    ::text,   '\x2ba592f78db6436527729929aaf6c908497cb200'::bytea),
('YETI'     ::text, 'PowerPool' ::text,    'CVP'	    ::text,   '\x38e4adb44ef08f22f5b5b76a8f0c2d0dcbe7dca1'::bytea),
('YPIE'     ::text, 'pieDAO'    ::text,    'CREAM'	    ::text,   '\x2ba592f78db6436527729929aaf6c908497cb200'::bytea),
('YPIE'     ::text, 'pieDAO'    ::text,    'aYFI'	    ::text,   '\x12e51e77daaa58aa0e9247db7510ea4b46f9bead'::bytea),
('YPIE'     ::text, 'pieDAO'    ::text,    'KP3R'	    ::text,   '\x1ceb5cb57c4d4e2b2433641b95dd330a33185a44'::bytea),
('YPIE'     ::text, 'pieDAO'    ::text,    'xSUSHI'     ::text,   '\x8798249c2e607446efb7ad49ec89dd1865ff4272'::bytea),
('YPIE'     ::text, 'pieDAO'    ::text,    'PICKLE'     ::text,   '\x429881672b9ae42b8eba0e26cd9c73711b891ca5'::bytea),
('YPIE'     ::text, 'pieDAO'    ::text,    'AKRO'	    ::text,   '\x8ab7404063ec4dbcfd4598215992dc3f8ec853d7'::bytea),
('YPIE'     ::text, 'pieDAO'    ::text,    'YFI'	    ::text,   '\x0bc529c00c6401aef6d220be8c6ea1667f6ad93e'::bytea),
('YPIE'     ::text, 'pieDAO'    ::text,    'SUSHI'	    ::text,   '\x6b3595068778dd592e39a122f4f5a5cf09c90fe2'::bytea)
;
