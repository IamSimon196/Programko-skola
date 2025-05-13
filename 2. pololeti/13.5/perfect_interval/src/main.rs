use std::io;

fn perfect_numbers(beg: u32, end: u32) -> Vec<u32> {
    let mut ans_list = Vec::new();
    
    for n in beg.max(2)..end {
        println!("Progress: {:.2}%", (n as f64 / (end - beg) as f64) * 100.0);
        
        if n % 2 != 0 { 
            continue;
        }
        let sum: u32 = (1..=n / 2).filter(|i| n % i == 0).sum();
        
        if sum == n {
            println!("Found perfect number: {}", n);
            ans_list.push(n);
        }
    }
    
    println!("Finished checking range.");
    ans_list
}

fn main() {
    let mut input = String::new();
    
    println!("Zadej pocatecni cislo:");
    io::stdin().read_line(&mut input).unwrap();
    let begin: u32 = input.trim().parse().unwrap();
    
    input.clear();
    println!("Zadej konecne cislo:");
    io::stdin().read_line(&mut input).unwrap();
    let end: u32 = input.trim().parse().unwrap();
    
    println!("Searching for perfect numbers in range {} - {}...", begin, end);
    let results = perfect_numbers(begin, end);
    
    println!("V intervalu {} - {} jsou dokonala cisla: {:?}", begin, end, results);
}
