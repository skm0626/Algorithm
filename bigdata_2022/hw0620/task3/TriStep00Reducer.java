package task3;

import java.io.IOException;
import java.util.ArrayList;
import java.util.StringTokenizer;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class TriStep00Reducer extends Reducer<IntPairWritable, IntWritable, IntWritable, IntWritable>{
  IntWritable ok = new IntWritable();
  IntWritable ov = new IntWritable();
   
   @Override
   protected void reduce(IntPairWritable key, Iterable<IntWritable> values,
         Reducer<IntPairWritable, IntWritable, IntWritable, IntWritable>.Context context) throws IOException, InterruptedException {
      
      ArrayList<Integer> neighbors = new ArrayList<Integer>();
      for(IntWritable v : values) {
//        String str = v.toString();
//        String[] arr = str.split("\t");
//        System.out.println(arr[1]);
//        int i = Integer.parseInt(arr[1]);
//        System.out.println(i);
        neighbors.add(v.get());
      }
      
//      for(int u : neighbors) {
//         for(int v : neighbors) {
//            if (u < v) {
//               ok.set(u, v);
//               context.write(ok, key);
//            }
//         }
      String str = key.toString();
      String[] arr = str.split("\t");
      int u = Integer.parseInt(arr[0]);
      int v = Integer.parseInt(arr[1]);
      if (u<v) {
        ok.set(u);
        ov.set(v);
        context.write(ok, ov);
      }
      
   }
}