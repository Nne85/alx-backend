import { createQueue } from 'kue';

const queue = createQueue();

const blackListed = ['4153518780', '4153518781']

const checkIfBlackListed = (phoneNumber) => {
    return blackListed.includes(phoneNumber);
}

const sendNotification = (phoneNumber, message, job, done) => {
    setTimeout(() => {
	job.progress(0, 100);
    if (checkIfBlackListed(phoneNumber)) {
	const error = new Error(`Phone number ${phoneNumber} is blacklisted`);
	done(error);
    };
    job.progress(50, 100);
	console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
	done();
    }, 1000)
}

queue.process('push_notification_code_2', (job, done) => {
    let {phoneNumber, message} = job.data;
    sendNotification(phoneNumber, message, job, done);
});
