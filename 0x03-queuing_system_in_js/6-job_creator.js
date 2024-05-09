import { createQueue } from 'kue';

const queue = createQueue();

const jobData = {
  phoneNumber: '08012345678',
  message: 'Welcome'
};
const job = queue.create('push_notification_code', jobData).save();

job.on('enqueue', () => {
  console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => console.log('Notification job completed'));

job.on('failed', (err) => {
  console.log('Notification job failed');
});
