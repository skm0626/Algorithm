package task1;

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
import task1.IntPairWritable;
import task1.TriCnt;
import task1.TriStep1Mapper;
import task1.TriStep1Reducer;

public class TriCnt extends Configured implements Tool {

    public static void main(String[] args) throws Exception {
        ToolRunner.run(new TriCnt(), args);
    }
    
    public int run(String[] args) throws Exception {
        
        String inputpath = args[0];
        String tmppath = inputpath + ".task31tritmp";
        String tmppath2 = inputpath + ".task312tritmp";
        String outpath = inputpath + ".task31triout";
        
        runStep0(inputpath, tmppath);
        runStep1(tmppath,tmppath2);
        runStep2(tmppath, tmppath2, outpath);
        
        return 0;
    }
    
    private void runStep0(String inputpath, String tmppath) throws Exception{
        
      Job job = Job.getInstance(getConf());
      job.setJarByClass(TriCnt.class);
      
      job.setMapOutputKeyClass(IntPairWritable.class);
      job.setMapOutputValueClass(IntWritable.class);
      
      job.setMapperClass(TriStep0Mapper.class);
      job.setReducerClass(TriStep0Reducer.class);
      
      job.setOutputKeyClass(IntWritable.class);
      job.setOutputValueClass(IntWritable.class);
      
      job.setInputFormatClass(TextInputFormat.class);
      job.setOutputFormatClass(SequenceFileOutputFormat.class);
        
        FileInputFormat.addInputPath(job, new Path(inputpath));
        FileOutputFormat.setOutputPath(job, new Path(tmppath));
        
        job.waitForCompletion(true);
        
    }
    
    private void runStep1(String tmppath, String tmppath2) throws Exception{
      
      Job job = Job.getInstance(getConf());
      job.setJarByClass(TriCnt.class);
      
      job.setMapOutputKeyClass(IntWritable.class);
      job.setMapOutputValueClass(IntWritable.class);
      
      job.setMapperClass(TriStep1Mapper.class);
      job.setReducerClass(TriStep1Reducer.class);
      
      job.setOutputKeyClass(IntPairWritable.class);
      job.setOutputValueClass(IntWritable.class);
      
      job.setInputFormatClass(SequenceFileInputFormat.class);
      job.setOutputFormatClass(SequenceFileOutputFormat.class);
        
        FileInputFormat.addInputPath(job, new Path(tmppath));
        FileOutputFormat.setOutputPath(job, new Path(tmppath2));
        
        job.waitForCompletion(true);
        
    }

    private void runStep2(String tmppath, String tmppath2, String outpath) throws Exception {
        
        Job job = Job.getInstance(getConf());
        job.setJarByClass(TriCnt.class);
        
        job.setReducerClass(TriStep2Reducer.class);
        
        job.setMapOutputKeyClass(IntPairWritable.class);
        job.setMapOutputValueClass(IntWritable.class);
        
        job.setPartitionerClass(TriCntPartitioner.class);
        
        job.setOutputFormatClass(TextOutputFormat.class);
        
        MultipleInputs.addInputPath(job, new Path(tmppath), SequenceFileInputFormat.class, TriStep2MapperForEdges.class);
        MultipleInputs.addInputPath(job, new Path(tmppath2), SequenceFileInputFormat.class, TriStep2MapperForWedges.class);
        
        FileOutputFormat.setOutputPath(job, new Path(outpath));
        
        job.waitForCompletion(true);
        
    }

}
