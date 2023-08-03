public class HammingReceptor {

    public static void main(String[] args) {
        String msg = "1000001";
        System.out.println("Original message: " + msg);
        String encodedMsg = encode(msg);
        System.out.println("Encoded message: " + encodedMsg);
    }

    public static String encode(String msg) {
        int parityBits = 4; // Number of parity bits for Hamming(11,7)
        int n = msg.length() + parityBits; // Length of final bit string

        // Create a StringBuilder to store the final message with parity bits
        StringBuilder encodedMsg = new StringBuilder();

        // Initialize all positions with parity bits to 0
        int j = 0; // current index in the original message
        for (int i = 0; i < n; i++) {
            if (isPowerOfTwo(i + 1)) {
                encodedMsg.append('0');
            } else {
                encodedMsg.append(msg.charAt(j));
                j++;
            }
        }

        // Calculate the parity bits
        encodedMsg = calculateParityBits(encodedMsg, parityBits);

        return encodedMsg.toString();
    }

    private static StringBuilder calculateParityBits(StringBuilder bits, int parityBits) {
        int n = parityBits;

        // Calculate parity for each parity bit
        for (int i = 0; i < n; i++) {
            int val = 0;
            for (int j = 1; j <= bits.length(); j++) {
                if ((j & (1 << i)) != 0) {
                    val = val ^ Character.getNumericValue(bits.charAt(bits.length() - j));
                }
            }

            // Insert parity bits at the correct positions
            bits.setCharAt((1 << i) - 1, Character.forDigit(val, 10));
        }
        return bits;
    }

    private static boolean isPowerOfTwo(int x) {
        return (x & (x - 1)) == 0;
    }
}
