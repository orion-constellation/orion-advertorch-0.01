import Verida from '@verida/cleint-ts'

document.getElementById('login').addEventListener('click'), async () => {
    try {
        const config = {
            environment: 'mainnet',
            appName: 'Adversarial Defence'
        }

    const client = new Verida.Client(config);
    await client.init();
    
    const did = await client.connect({
        logo: 'https://raw.githubusercontent.com/verida/verida-examples/main/pytorch-adversarial/frontend/adversarial-exp/src/assets/logo.png',,
        description: 'An experiment in adversarial robustness and traffic',
    });

    console.log("User DID:", did);

    // Interact with the datastore
} catch (error) {
    console.error("Error Initializing Verida client:", error);
}}