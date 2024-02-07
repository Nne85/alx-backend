import { createQueue } from 'kue';


const queue = createQueue({name: 'push_notification_code_3'});

const createPushNotificationsJobs = (jobs, queue) => {
    if(!Array.isArray(jobs)) {
	new Error ('Jobs is not an array');
    }

    jobs.forEach((job) => {
	let newJob = queue.create('push_notification_code_3', job);
	newJob
	    .on('enqueue', () => {
		console.log(`Notification job created: ${newJob.id}`);
	    })
	    .on('progress', (progress, data) => {
		console.log(`Notification job ${newJob.id} ${progress}% complete`);
	    })
	    .on('complete', () => {
		console.log(`Notification job ${newJob.id} completed`);
	    })
	    .on('failed', (error) => {
		console.log(`Notification job ${newJob.id} failed: ${error}`);
	    })
	newJob.save();
    });
}

export default createPushNotificationsJobs;
