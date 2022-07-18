package task3;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.mapreduce.Partitioner;
import task3.IntPairWritable;

public class TriCntPartitioner extends Partitioner<IntPairWritable, IntWritable>{
  public int getPartition(IntPairWritable key, IntWritable value, int numReduceTasks) {
      return (key.u * 31 + key.v) % numReduceTasks;
  }
}