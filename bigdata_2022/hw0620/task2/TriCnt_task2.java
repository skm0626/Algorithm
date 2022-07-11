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

public class TriCnt_task2 extends Configured implements Tool {

    public static void main(String[] args) throws Exception {
        ToolRunner.run(new TriCnt_task2(), args);
    }
    
    public int run(String[] args) throws Exception {
        
        String inputpath = args[0];
        String tmppath = inputpath + ".task2tmp";
        String outpath = inputpath + ".task2out";
        
        runStep1(inputpath, tmppath);
        runStep2(inputpath, tmppath, outpath);
        
        return 0;
    }
    
    private void runStep1(String inputpath, String tmppath) throws Exception{
        
      Job job = Job.getInstance(getConf());
      job.setJarByClass(TriCnt_task2.class);
      
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

    private void runStep2(String inputpath, String tmppath, String outpath) throws Exception {
        
        Job job = Job.getInstance(getConf());
        job.setJarByClass(TriCnt_task2.class);
        
        job.setReducerClass(TriStep01Reducer.class);
        
        job.setMapOutputKeyClass(IntWritable.class);
        job.setMapOutputValueClass(IntPairWritable.class);
        
//        job.setPartitionerClass(TriCntPartitioner.class);
        
        job.setOutputFormatClass(TextOutputFormat.class);
        
        MultipleInputs.addInputPath(job, new Path(tmppath), SequenceFileInputFormat.class, TriStep01Mapper.class);
//        MultipleInputs.addInputPath(job, new Path(tmppath), SequenceFileInputFormat.class, TriStep2Mapper1.class);
        
        FileOutputFormat.setOutputPath(job, new Path(outpath));
        
        job.waitForCompletion(true);
        
    }

    

}
