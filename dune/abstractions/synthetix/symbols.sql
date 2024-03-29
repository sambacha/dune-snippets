CREATE TABLE IF NOT EXISTS synthetix.symbols (symbol text, address bytea,
                                              block_time timestamptz,
                                              PRIMARY KEY (symbol, address));
INSERT INTO synthetix.symbols
    VALUES ('sAUD', '\xB03dFc4b9C9756B6D4Fbc12DAde7732149Fcf00d'),
    ('sAUD', '\x710882750DDe5DBc64e5a7df23a8cF068dF74910'),
    ('sAUD', '\xa6FE80c4c4AADb4B33dB7f22dc9AE2C4697cC406'),
    ('sAUD', '\xACa2179a884bAC7C3D0bc4131585E1B7DbDD048e'),
    ('sAUD', '\xe04d8770Dc06135Dd97214ea8bcbf7B1CC057AA3'),
    ('sBRL', '\xa5A4ccCCcAa26Cea096F6E493839423F4D66c63F'),
    ('sBTC', '\xf8AD89091B2724bdb7528c50B282B565Db4635bb'),
    ('sBTC', '\x832177F21CCDcc286003faDF4e98fc11dc5C627F'),
    ('sBTC', '\x6bCd1caE4A3c099c696B51f889bE2120DF62b7c0'),
    ('sBTC', '\xF0ac210915BD88Ea51c9EB800a4078a85927efdF'),
    ('sBTC', '\x17628A557d1Fc88D1c35989dcBAC3f3e275E2d2B'),
    ('sCAD', '\x8f69c9Ee79Bf9320E1A5C19e559108E1cb3d002B'),
    ('sCHF', '\x9270D9970D6ACA773e2FA01633CDc091a46714c9'),
    ('sCHF', '\x296b019E6dF25Ce3b71d4239b8C7CEc1a417d4E9'),
    ('sCHF', '\xfF0b8894CC44F300e124bcd39F95555816b8B1d5'),
    ('sCHF', '\x64C73355FBD0274e677609E8fb372427DF975508'),
    ('sCHF', '\x253914cf059f4c3E277c28060C404acFc38FB6e2'),
    ('sCNY', '\x60C34eB93AFCd1B701fF8C036B128441C68A8A70'),
    ('sEUR', '\xC2bb52457D81FBD223CC92b44cd372d36b338A10'),
    ('sEUR', '\x45AA2F706C3d695aCC1DA9698Fb803b8Ef5157ba'),
    ('sEUR', '\x68473dc4B7A4b0867fd7C5b9A982Fea407DAD320'),
    ('sEUR', '\x57e4A2D7D9b759Cf6FA2C937D52E408c66fB6384'),
    ('sEUR', '\x2fB419E7023b32201e9aB3aba947f5c101a5C30e'),
    ('sGBP', '\xdB36B8f25bB1f289d97aeE8f87BAcCaC58fA8883'),
    ('sGBP', '\x0a24864596C54D79C825e64b281645249C14590C'),
    ('sGBP', '\xD8C733Ac0B2Db47BbA7af7716Eb696e62C417D5b'),
    ('sGBP', '\x486e27D56c0744970687927728598F8B96451Cc4'),
    ('sGBP', '\x8FA7FBb0144CeA832a76547aEAB1Ad8d9e4588F1'),
    ('sGBP', '\xB3098Ae40f488ffdb979827Fd01597CC20c5a5A0'),
    ('sINR', '\x51671B7556EbEB4c43180e983F5569973e15cAc9'),
    ('sJPY', '\xD9E5A009Ec07dE76616d7361Ed713eF434d71325'),
    ('sJPY', '\x11Dfa1Bf994Ea47e361eC474519Afd627e932eb0'),
    ('sJPY', '\x4B1cE9C42A381CB2d74ffeF20103e502e2fc619C'),
    ('sJPY', '\x68043c3EAE66Ac1c28341867491E615412fc84FD'),
    ('sJPY', '\x8ed1B71B00DbaB96A6db6DF0C910f749243de6D3'),
    ('sKRW', '\xdF846D3ded30A0590319f8A7ECD4e233B0e9188C'),
    ('sNZD', '\xCF401f31c63F58DEbfC76F441731dfa945cd0Bde'),
    ('sPLN', '\x1943dBd2A793c588B5170188Ee6fb62E02AfdfF7'),
    ('sRUB', '\x8a8DcbBa6038c6Fc6D192F5cf5C5dD83B98591bc'),
    ('sSGD', '\x2aE393C18b6Aa62D6a2250aF7b803Fa6973bC981'),
    ('sUSD', '\x0cBE2dF57CA9191B64a7Af3baa3F946fa7Df2F25'),
    ('sUSD', '\xd8B325e9a95aBc44cEdc90AAb64ec1f231F2Cc8f'),
    ('sUSD', '\x2656a6E566f8e60f444B283bf346fC74A9990c96'),
    ('sUSD', '\x289e9a4674663decEE54f781AaDE5327304A32f8'),
    ('sUSD', '\x2A020C1ad728f1C12735bC4877CEECa4491A4a3D'),
    ('sUSD', '\xAe38b81459d74A8C16eAa968c792207603D84480'),
    ('sXAG', '\x4D57A8212BDb8bdca049365BCE8afA0244a0E3FC'),
    ('sXAG', '\xD6308849094c5E6Eb0EDAba255A06Ca32B0106Bf'),
    ('sXAG', '\x3A412043939d9F7e53373b64f858ecB870a92E50'),
    ('sXAG', '\xd415e342a5C7Ee189D939b4DC17E85880fE1096A'),
    ('sXAG', '\x1B9d6cD65dDC981410cb93Af91B097667E0Bc7eE'),
    ('sXAU', '\x112D5fA64e4902B6ff1a35495a0f878c210A5601'),
    ('sXAU', '\x4a15d9dfC95ba7B9e33CE70e7E0762dc8F7AC237'),
    ('sXAU', '\x4d96b67f5BDe58A622D9bF2B8a1906C8B084fAf4'),
    ('sXAU', '\x00aB7c26A5a6C4C32D0b897E4Af3CB32F92aad34'),
    ('sXAU', '\xA408d8e01C8E084B67559226C5B55D6F0B7074e2'),
    ('XDR', '\x2972705AF18c66c14CDd27AD412961E01944A9C3'),
    ('XDR', '\x6025f88ABB6d99d02c5EEd82C151d52Bac8E444b'),
    ('XDR', '\x30A46E656CdcA6B401Ff043e1aBb151490a07ab0'),
    ('XDR', '\x96f9D144E55149437640512B82d7Dda065E89773'),
    ('sETH', '\x42456D7084eacF4083f1140d3229471bbA2949A8'),
    ('sETH', '\x8519d1BDb4cC1753DF95C6E98F6Bd0E95dE568D9'),
    ('sETH', '\x0577d4268ABE6777aE37688D015598819088297B'),
    ('sETH', '\xD81AdA188331e627567BBEF80F91217cd3109592'),
    ('sETH', '\x9f71b6596b2C9d357f9F04F8cA772fbD6e2c211C'),
    ('sETH', '\xD0DC005d31C2979CC0d38718e23c82D1A50004C0'),
    ('sBNB', '\xC906de7f8b4C1a4787023F50F49CE98F9F67c4b8'),
    ('sBNB', '\x33cE216C10dEA5E724b7A90628ce7853eef127B3'),
    ('sBNB', '\xE5787927410b659cc4eA2441cDaa361f9D7b250C'),
    ('sBNB', '\xaE3971E603b11dA40aea85d8c2355150c7c47683'),
    ('sBNB', '\xadaD43Be81E2206f6D1aF4299cA2a029e16af7AB'),
    ('iBTC', '\xd8f6B6b6782632275B2B51230654f687f5b12Cde'),
    ('iBTC', '\xccC395f0eBFAA26dCC2D3BACc23d55614002236b'),
    ('iBTC', '\xCe88906100c145522Be3a509683881241aBb3C52'),
    ('iBTC', '\x83266A95429b903cC5e954bF61c7eddf8a52b971'),
    ('iBTC', '\x810425566d1d3078B15A6f035b17886F18F3c54B'),
    ('iBTC', '\xc704c9AA89d1ca60F67B3075d05fBb92b3B00B3B'),
    ('iETH', '\x51Fe40e6292dbC44623b298a4086ffA6f5976ba1'),
    ('iETH', '\x9b461df6fc38E1baEC08c06EB9e916093af8d11C'),
    ('iETH', '\x3f3804176D90640aC6063124afd4bc0636aC85B6'),
    ('iETH', '\xf53B56B6Fb98aaF514bcd28f6Fa6fd20C24E5c22'),
    ('iETH', '\xc0bA711B4E128425Be9245ce750D82c90b42D6D2'),
    ('iETH', '\xaE55F163337A2A46733AA66dA9F35299f9A46e9e'),
    ('iBNB', '\x56751D5Ac7D2B614C79d22e6b52D3285cFA8a293'),
    ('iBNB', '\xED4A3Adffa428fFD126AeD8ba5b8B58bb12c11ca'),
    ('iBNB', '\x57Ff288dd9D478b046647A5aB917195449F1F6e5'),
    ('iBNB', '\x09400Ec683F70174E1217d6dcdBf42448E8De5d6'),
    ('iBNB', '\xc68b5Eb9e035b2B84568A4C6201e3b200C0236ba'),
    ('iBNB', '\xf86048DFf23cF130107dfB4e6386f574231a5C65'),
    ('sMKR', '\x13586160e4F890D0631c3C08D989f5b7AFe202b0'),
    ('sMKR', '\xFAc2B3400Df00a348C3118831a45A05255F9004A'),
    ('sMKR', '\x84965DCa28c4Eb9dE61d80f80e811eA12BE1c819'),
    ('sMKR', '\x54A0326fB698c2CFACa5327550a897FA66d21f07'),
    ('sMKR', '\xD1599E478cC818AFa42A4839a6C665D9279C3E50'),
    ('sTRX', '\xa6e5DA838D3b8338783E0710E1D5F6C8e8E998CE'),
    ('sTRX', '\x0dA04b80e21B344fCFD49C04bEC658E80F1D7428'),
    ('sTRX', '\x1A60E2E2A8BE0BC2B6381dd31Fd3fD5F9A28dE4c'),
    ('sTRX', '\x3d0e7c09242b0cAd4e81cB2f6D2183EF517500EF'),
    ('sTRX', '\xC4Be4583bc0307C56CF301975b2B2B1E5f95fcB2'),
    ('sXTZ', '\x6E5Bc3e877CFaa06eF97dfA12e63EfbB8FCbb03e'),
    ('sXTZ', '\xC0b1F43Ee7b0670F7B34e14c4702e54a905A51B5'),
    ('sXTZ', '\xe109da5361299eD96D91146B8Cc12F682D21964e'),
    ('sXTZ', '\x2CB1B47fB16013798086f267E04E6579dcb72A74'),
    ('sXTZ', '\x91DBC6f587D043FEfbaAD050AB48696B30F13d89'),
    ('iMKR', '\x99bcc501d04F400Ba3F78b5375D00B56acE6Ee0D'),
    ('iMKR', '\x047FC84504714d526808Be07BF17Bdd70726ef92'),
    ('iMKR', '\xD95e7F80766580634B2E0E49d9F66af317994FC7'),
    ('iMKR', '\x10A0532DE3C86D9cE810F004FaBcf5a1EA464390'),
    ('iMKR', '\x1228c7D8BBc5bC53DB181bD7B1fcE765aa83bF8A'),
    ('iTRX', '\x87ea2450EaB99A74e55E2B446290011765393AC1'),
    ('iTRX', '\x80eDAC70ec108a9c5B47972da9924397Ba974Ff9'),
    ('iTRX', '\x406555dbF02e9E4df9AdeAeC9DA76ABeED8C1BC3'),
    ('iTRX', '\x2DE37AF5BA64f5CaE3202Bf13dbEDc4D46e8046f'),
    ('iTRX', '\xdD87cbDe3C1f8F728C7924c8C9C983Af6dfcfeA8'),
    ('iXTZ', '\xFE6Cd6dE459db214818492f532Ec02Ba87319437'),
    ('iXTZ', '\x72661E76475354403838EB04144206f70Ff97d79'),
    ('iXTZ', '\xAD7258d0054c03112a4f5489A4B24eC34a2fc787'),
    ('iXTZ', '\x59D39e14cC735b39746c94351E7fbDd92C8D0d3C'),
    ('iXTZ', '\x6dFDFbfB4B180be4482F8b753fb33720C2831a9f'),
    ('sCEX', '\x6aa0f8620614aFe9BD4aBA3148439b08eb2557C0'),
    ('sCEX', '\x93CfF799F255eDa2089cFB3F05696B5B66873C1A'),
    ('sCEX', '\x8a3ca1d2d9a05683EB4DB447d0e3122Fec09d9ee'),
    ('sCEX', '\x2420057461bD2fb756e0A610897c51De7fB18311'),
    ('sCEX', '\x5eA2544551448cF6DcC1D853aDdd663D480fd8d3'),
    ('iCEX', '\x66B86625ee80b06e94E027e44eA35680a0730233'),
    ('iCEX', '\x43e1505E315BE6C8b875a37F7D8753Ba84140A37'),
    ('iCEX', '\xDa5eD43B9B6E36b4f27cc6D8c1974532cdBd55F9'),
    ('iCEX', '\xf7011510572d0EFE31d1E90cd6dc1EF84e6B13b8'),
    ('iCEX', '\x817c39c8825e12eA7752483c85dd2c800b78B357'),
    ('sXRP', '\xFf6866FF46c71706DcD5A0A38f12279553bE6233'),
    ('sXRP', '\xC64CdA66Bc1d026b984D6BEE6aDBf71eAc8A099d'),
    ('sXRP', '\x4dc1E8bAcc26D563941dCB59c72BD9FE58663778'),
    ('sXRP', '\xF5d0BFBc617d3969C1AcE93490A76cE80Db1Ed0e'),
    ('sLTC', '\x8e0cC15bBCd10E170AC07982B5D6930502C63784'),
    ('sLTC', '\x088256945480c884C067a8Bc98A72A1C984f826B'),
    ('sLTC', '\x79BEf89A63bE04A75F1fA42E8f42ad873B6f43e2'),
    ('sLTC', '\x6cF29c515A33209c6eCa43c293004ac80c0614f0'),
    ('sLINK', '\x34B19046c6657D26B0C9b63d3Fb54C2754Ed4537'),
    ('sLINK', '\x46824bFAaFd049fB0Af9a45159A88e595Bbbb9f7'),
    ('sLINK', '\x3D663Dbe79fA9752815e03e129D6703eDE1C6D71'),
    ('sLINK', '\xAf918f4a72BC34E59dFaF65866feC87947F1f590'),
    ('sDEFI', '\x4917E9Ef69E3a1C82651c9158cA2c25b3A564760'),
    ('sDEFI', '\xF778Ec504245EfE1eA010C5C3E50b6F5f5E117da'),
    ('sDEFI', '\xE725d6Ff29d0679C9Cb6Fa8972a1E8a7FB49610B'),
    ('sDEFI', '\xf5a6115Aa582Fd1BEEa22BC93B7dC7a785F60d03'),
    ('iXRP', '\xcBBb17D9767bD57FBF4Bbf8842E916bCb3826ec1'),
    ('iXRP', '\xd7adF1b5E31D1C40E08F16a2095338ce3aA8f2Fc'),
    ('iXRP', '\xccda7941aB1AC7a32F49843c0b3EDF618b20F6Ae'),
    ('iXRP', '\x71Cd588eFA3609bc14E7B0c7C57dDDfd3a72E8a2'),
    ('iLINK', '\xEC114001D23eeFE6624Fb42cCbF4b3c793e295f1'),
    ('iLINK', '\x3DdF5dAd59F8F8e8f957709B044eE84e87B42e25'),
    ('iLINK', '\x8c6680412e914932A9abC02B6c7cbf690e583aFA'),
    ('iLINK', '\x63d630B6D89c21E171E86c51C7243284510DBd79'),
    ('iLTC', '\x05DD55C18999b4a2f905978C029B85dA37750170'),
    ('iLTC', '\xec98BB42C8F03485bf659378da694512a16f3482'),
    ('iLTC', '\xfca2e82E5414c695c81b99D753b0b11c50bDC93D'),
    ('iLTC', '\x0f5BdfD0958345C2e7Adb1741024aEd6Dd159e6C'),
    ('iDEFI', '\x8E39e807D9eaE1cED9BCE296F211c38BA5ab2f9B'),
    ('iDEFI', '\xC5Bfbc63dc8D36E81434e93e0ee097999879d7F4'),
    ('iDEFI', '\xaE7D62Fb6a305E6d9E9F8c43bbb41093c2bE52f6'),
    ('iDEFI', '\x489d4D4c4bC781EAab3A36C44d66762Ceb6e1e2D'),
    ('sEOS', '\x31a9c51eEd5282F11ae5CDD061A65A4ce0346C08'),
    ('sBCH', '\x9b68b85c61B082B2495B342F26B20a57cFd73D26'),
    ('sETC', '\x2369D37ae9B30451D859C11CAbAc70df1CE48F78'),
    ('sDASH', '\xc66499aCe3B6c6a30c784bE5511E8d338d543913'),
    ('sXMR', '\x86FD9c0261E804476bA11056fFD758da2469ed56'),
    ('sADA', '\x1Cda42C559D2EB137103D9A01d1ae736dEDA3aEF'),
    ('sFTSE', '\x8D34924EAe7578692775fDd94Ed27bc355397E4a'),
    ('sNIKKEI', '\x4CeB220C5E38E27ef5187F7ab853aC182D233d39'),
    ('iEOS', '\xc66a263f2C7C1Af0bD70c6cA4Bff5936F3D6Ef9F'),
    ('iBCH', '\x0E87a320daCE86A0b427FA2Bae282dE5c7697278'),
    ('iETC', '\xF13f9E75913b352622F8AEEA5Ac32498b1C228d0'),
    ('iDASH', '\x5f7A299Be82D8f5A626300c62C477b233F616121'),
    ('iXMR', '\xC5D2b3f5DAf11B6111Af86a72A5938B0fE6c5045'),
    ('iADA',
     '\x9D4193187B247a400E8D8ba716F1C18c0dC65528')ON CONFLICT DO NOTHING;

CREATE OR REPLACE FUNCTION synthetix.insert_symbols (
    start_ts timestamptz,
    end_ts timestamptz
    = now ()) RETURNS integer LANGUAGE plpgsql AS $function$ DECLARE r integer;
BEGIN
WITH rows
AS (INSERT INTO synthetix.symbols SELECT
        trim ('\000' from encode ("currencyKey", 'escape')) AS symbol,
    synth AS address,
    evt_block_time AS block_time FROM
            synthetix."Issuer_evt_SynthAdded" WHERE evt_block_time
        >= start_ts AND evt_block_time < end_ts

            UNION

                SELECT trim ('\000' from encode ("currencyKey", 'escape'))
                    AS symbol,
    synth AS address,
    evt_block_time AS block_time FROM
            synthetix."Issuer_v2_27_2_evt_SynthAdded" WHERE evt_block_time
        >= start_ts AND evt_block_time < end_ts

            UNION

                SELECT trim ('\000' from encode ("currencyKey", 'escape'))
                    AS symbol,
    synth AS address,
    evt_block_time AS block_time FROM
            synthetix."Issuer_v2_28_4_evt_SynthAdded" WHERE evt_block_time
        >= start_ts AND evt_block_time < end_ts

            UNION

                SELECT trim ('\000' from encode ("currencyKey", 'escape'))
                    AS symbol,
    synth AS address,
    evt_block_time AS block_time FROM
            synthetix."Issuer_v2_30_0_evt_SynthAdded" WHERE evt_block_time
        >= start_ts AND evt_block_time < end_ts

            UNION

                SELECT trim ('\000' from encode ("currencyKey", 'escape'))
                    AS symbol,
    synth AS address,
    evt_block_time AS block_time FROM
            synthetix."Issuer_v2_31_1_evt_SynthAdded" WHERE evt_block_time
        >= start_ts AND evt_block_time < end_ts

            UNION

                SELECT trim ('\000' from encode ("currencyKey", 'escape'))
                    AS symbol,
    synth AS address,
    evt_block_time AS block_time FROM
            synthetix."Issuer_v2_35_2_evt_SynthAdded" WHERE evt_block_time
        >= start_ts AND evt_block_time < end_ts

            UNION

                SELECT trim ('\000' from encode ("currencyKey", 'escape'))
                    AS symbol,
    synth AS address,
    evt_block_time AS block_time FROM
            synthetix."Issuer_v2_36_0_evt_SynthAdded" WHERE evt_block_time
        >= start_ts AND evt_block_time
        < end_ts ON CONFLICT DO NOTHING RETURNING 1) SELECT
    count (*) INTO r from rows;
RETURN r;
END $function$;

SELECT synthetix.insert_symbols ('2019-01-01',
                                 (SELECT max (time) FROM ethereum.blocks));

INSERT INTO cron.job (schedule, command) VALUES (
    '3 0 * * *',
    'SELECT synthetix.insert_symbols((SELECT max(block_time) FROM synthetix.symbols));')
    ON CONFLICT (command) DO UPDATE SET schedule = EXCLUDED.schedule;
