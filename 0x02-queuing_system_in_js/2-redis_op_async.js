import { createClient } from 'redis';
import {print} from 'redis';
import { promisify } from 'util';

const client = createClient();
const getClient = promisify(client.get).bind(client);

client.on('error', (err) => console.log('Redis client not connected to the server:', err));
client.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
    client.set(schoolName, value);
    print("Confirmation!: value set!")
}

const displaySchoolValue = async (schoolName) => {
    const res = await getClient(schoolName);
    console.log(res);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
