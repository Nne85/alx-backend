import { createQueue } from 'kue';


const queue = createQueue();


const job = queue.create('push_notification_code', {
  phoneNumber: "+233201775908",
  message: "Account verified successfully",
});

job
    .on('enqueue', () => {
	console.log('Notification job created:', job.id);
    })
    .on('complete', () => {
	console.log('Notification job completed');
    })
    .on('failed attempt', () => {
	console.log('Notification job failed');
    });

job.save();
