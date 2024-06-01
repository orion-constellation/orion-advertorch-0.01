import { Network } from '@verida/client-ts';
import { EnvironmentType } from '@verida/types';
import { VaultAccount } from '@verida/account-web-vault';

const VERIDA_ENVIRONMENT = EnvironmentType.TESTNET;
const CONTEXT_NAME = 'My Application Context Name';

// The LOGO_URL should be a 170x170 PNG file
const LOGO_URL = "https://assets.verida.io/verida_login_request_logo_170x170.png";

const account = new VaultAccount({
    logoUrl: LOGO_URL
});

const context = Network.connect({
    client: {
        environment: VERIDA_ENVIRONMENT,
    },
    account: account,
    context: {
        name: CONTEXT_NAME,
    },
});