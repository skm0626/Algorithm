package task2;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.mapreduce.Partitioner;

public class TriCntPartitioner extends Partitioner<IntWritable, IntPairWritable>{
	public int getPartition(IntWritable key, IntPairWritable value, int numReduceTasks) {
		return (value.u * 31 + value.v) % numReduceTasks;
	}
}
