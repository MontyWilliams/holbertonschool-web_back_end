import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([
    uploadPhoto(),
    createUser()])
    .then((boop) => {
      console.log(
        `${boop[0].body} ${boop[1].firstName} ${boop[1].lastName}`,
      );
    }).catch(() => console.log('Signup system offline'));
}
