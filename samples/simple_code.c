void my_function(char *data, unsigned int length, const char key[32]) {
	int i;
	for (i = 0; i < length; i++) {
		data[i] ^= key[i % 32];
	}
}
