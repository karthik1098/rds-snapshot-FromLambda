var AWS = require('aws-sdk');

const rdsConfig = {
    apiVersion: '2014-10-31',
    accessKeyId: process.env.ACCESS_KEY,
    secretAccessKey: process.env.SECRET_KEY,
    region: process.env.REGION
}

const rds = new AWS.RDS(rdsConfig);

exports.handler = (event, context, callback) => {

  const currentDate = new Date();
  
  const params = {
      DBInstanceIdentifier: 'database-1', 
      DBSnapshotIdentifier: `database-1-${currentDate.toDateString().replace(/\s+/g, '-').toLowerCase()}-snapshot-manual-by-lamda`, 
    };

  rds.createDBSnapshot(params, function(err, data) {
      if (err) {
          console.log(err, err.stack);        // an error occurred
          callback(err)
      }
      else {
        callback(null, data);// successful response
        console.log("Snapshot Created ...");
      }
    });
}