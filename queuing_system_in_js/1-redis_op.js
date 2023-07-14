import * as redis from 'redis';
import { createClient } from 'redis';

const client = createClient({
  host: 'localhost',
})

client.connect();

client.on('connect', () => console.log('Redis client connected to the server'))
client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

const setNewSchool = (schoolName, value) => {
  client.SET(schoolName, value, redis.print)
}

const displaySchoolValue = (schoolName) => {
  client.GET(schoolName, (err, res) => {
    if(err) {
      console.log(err);
    } else {
      console.log(res)
    }
  })
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
