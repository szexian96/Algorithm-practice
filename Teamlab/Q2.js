const divisor_sum = (num, limit) => {
 
  let sum = 0; // 求める合計値
  const sqrtNum = Math.sqrt(num); // num の平方根
  
  for (let d = 1; d <= limit; ++ d) {       
    
    if (d > sqrtNum)  // dがnumの平方根を超えたらループから抜ける
      break;    
    
    if (num % d === 0) {// d が num の約数である
      sum += d;// sum にdを加算
      const q = num / d;  // sum を d で割った商を求める（整数になる）
      if (q <= limit && q !== d) {  // qがlimit以下であり、かつ qとdが等しくない場合
        sum += q;// 商qもsumに加算
      }
    }
  }
  
  return sum;
}


// テスト実行
console.log(divisor_sum(60, 18)); // => 58  (約数かどうかを調べるのは、7までで済む)
console.log(divisor_sum(1234567890, 5000000));// => 1734174　(約数かどうかを調べるのは、35136までで済む)
console.log(divisor_sum(100, 30)); // => 67 (約数かどうかを調べるのは、10までで済む。100は10の２乗なので、10を２回足さないようにする。)
console.log(divisor_sum(60, 5)); // => 15 (この場合は、5は√60より小さいので、1以上5以下の全ての整数について60の約数かどうかを調べる)