	.section	.data
msg:
	.string	"Hello world!\n"

	.section .text
	.globl	_start
_start:
	# Print to stdout
	mov $1, %rax # sys_write syscall
	mov $1, %rdi # fd 1 is stdout
	lea	msg(%rip), %rsi # copy "msg" to %rsi
	mov $13, %rdx # length of "msg"
	syscall

	# Exit the program with return code 69
	mov	$60, %rax
	mov $0, %rdi
	syscall
