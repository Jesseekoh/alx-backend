import { createClient } from 'redis';

const client = createClient();

client.on_connect('error', (err) => console.log('Redis client Error', err));
client.on('connect', () => console.log('Redis client connected to the server'));
