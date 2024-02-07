// Importing the node_redis library using ES6 syntax
import redis from 'redis';
import { promisify } from 'util';

// Create a Redis client
const client = redis.createClient();

// Event handler for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
})

// Event handler for connection errors
client.on('error', (err) => {
  console.error(`Redis client not connected to the server:, ${err}`);
})

// Promisify the get function of Redis client
const getAsync = promisify(client.get).bind(client);

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
}

// Function to display the value for a school key in Redis
const displaySchoolValue = async (schoolName) => {
  try {
	  const reply = await getAsync(schoolName);
	  console.log(reply)
  } catch(error) {
	  console.error(error);
  }
};

const call = async () => {
	await displaySchoolValue('Holberton');
        setNewSchool('HolbertonSanFrancisco', '100');
        await displaySchoolValue('HolbertonSanFrancisco');
}

call();
