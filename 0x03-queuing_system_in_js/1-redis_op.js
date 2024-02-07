// Importing the node_redis library using ES6 syntax
import redis from 'redis';

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

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
}

// Function to display the value for a school key in Redis
const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (err, reply) => {
      console.log(reply);
  });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
