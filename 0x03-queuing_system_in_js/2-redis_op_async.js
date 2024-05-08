import redis, { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('error', (err) =>
  console.log(`Redis client not connected to the server: ${err}`)
);

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

const displaySchoolValue = async (schoolName) => {
  console.log(await promisify(client.get).bind(client)(schoolName));;
};

async function main () {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}

client.on('connect', async () => {
  console.log('Redis client connected to the server');
  await main();
});