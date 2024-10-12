	.section	.data
msg:
	.string	"Hello world!\n"

	.section .text
	.globl	_start
_start:
	# Print to stdout
	mov $1, %rax
	mov $1, %rdi
	lea	msg(%rip), %rsi
	mov $13, %rdx
	syscall

	# Exit the program with return code 69
	mov	$60, %rax
	mov $0, %rdi
	syscall
