package task2;

import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.MultipleInputs;
import org.apache.hadoop.mapreduce.lib.input.SequenceFileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.SequenceFileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

public class TriCnt_task2_2 extends Configured implements Tool {

    public static void main(String[] args) throws Exception {
        ToolRunner.run(new TriCnt_task2_2(), args);
    }
    
    public int run(String[] args) throws Exception {
        
        String inputpath = args[0];
        String tmppath = inputpath + ".task22tmp";
        String tmppath2 = inputpath + ".task223tmp";
        String outpath = inputpath + ".task22out";
        
        runStep1(inputpath, tmppath);
        runStep2(tmppath, tmppath2);
        runStep3(tmppath2, outpath);
        
        return 0;
    }
    
    private void runStep1(String inputpath, String tmppath) throws Exception{
        
      Job job = Job.getInstance(getConf());
      job.setJarByClass(TriCnt_task2_2.class);
      
      job.setMapOutputKeyClass(IntPairWritable.class);
      job.setMapOutputValueClass(IntWritable.class);
      
      job.setMapperClass(TriStep00Mapper.class);
      job.setReducerClass(TriStep00Reducer.class);
      
      job.setOutputKeyClass(IntWritable.class);
      job.setOutputValueClass(IntWritable.class);
      
      job.setInputFormatClass(TextInputFormat.class);
      job.setOutputFormatClass(SequenceFileOutputFormat.class);
        
      FileInputFormat.addInputPath(job, new Path(inputpath));
      FileOutputFormat.setOutputPath(job, new Path(tmppath));
      
      job.waitForCompletion(true);
        
    }

    private void runStep2(String tmppath, String tmppath2) throws Exception {
        
        Job job = Job.getInstance(getConf());
        job.setJarByClass(TriCnt_task2_2.class);
        
        job.setReducerClass(TriStep01Reducer.class);
        
        job.setMapOutputKeyClass(IntWritable.class);
        job.setMapOutputValueClass(IntPairWritable.class);
        
//        job.setPartitionerClass(TriCntPartitioner.class);
        job.setOutputKeyClass(IntPairWritable.class);
        job.setOutputValueClass(IntPairWritable.class);
        
        job.setOutputFormatClass(SequenceFileOutputFormat.class);
        
        MultipleInputs.addInputPath(job, new Path(tmppath), SequenceFileInputFormat.class, TriStep01Mapper.class);
//        MultipleInputs.addInputPath(job, new Path(tmppath), SequenceFileInputFormat.class, TriStep2Mapper1.class);
        
        FileOutputFormat.setOutputPath(job, new Path(tmppath2));
        
        job.waitForCompletion(true);
        
    }
    
    private void runStep3(String tmppath2, String outpath) throws Exception {
      
      Job job = Job.getInstance(getConf());
      job.setJarByClass(TriCnt_task2_2.class);
      
      job.setReducerClass(TriStep02Reducer.class);
      
      job.setMapOutputKeyClass(IntPairWritable.class);
      job.setMapOutputValueClass(IntPairWritable.class);
      
//      job.setPartitionerClass(TriCntPartitioner.class);
      
      job.setOutputFormatClass(TextOutputFormat.class);
      
      MultipleInputs.addInputPath(job, new Path(tmppath2), SequenceFileInputFormat.class, TriStep02Mapper.class);
//      MultipleInputs.addInputPath(job, new Path(tmppath), SequenceFileInputFormat.class, TriStep2Mapper1.class);
      
      FileOutputFormat.setOutputPath(job, new Path(outpath));
      
      job.waitForCompletion(true);
      
  }

    

}
