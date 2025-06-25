package isprime

@export
isprime :: proc "c" (num: int) -> bool {

    if num == 0 || num == 1{
        return false
    }

    for i in 2 ..< num {
		if num % i == 0 {
			return false 
		}
	}
	return true 
}
