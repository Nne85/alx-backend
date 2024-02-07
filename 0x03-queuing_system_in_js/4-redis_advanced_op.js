import { createClient, print } from 'redis';


const client = createClient();

client.on('connect', () => {
    console.log("Redis client connected to the server");
})

client.on('error', (error) => {
    console.log("Redis client not connected to the server: ${error}");
})

const sethash = (key, fieldName, fieldValue) => {
    client.hset(key, fieldName, fieldValue, print);
};

const getAllHash = (hashName) => {
    client.HGETALL(hashName, (error, res) => {
	console.log(res)
    })
};

const hashKey = {
	'Portland': 50,
	'Seattle': 80,
	'New York': 20,
	'Bogota': 20,
	'Cali': 40,
	'Paris':2
}

for (const [key, value] of Object.entries(hashKey)) {
    sethash('HolbertonSchools', key, value);
}

getAllHash('HolbertonSchools');
