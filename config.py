# define the parameters for the filter generation and to convert it to HDL

def get_args(parser):
    parser.add_argument("--number-of-taps", type = int, default = 40, help = "The number of taps of the FIR filter")
    parser.add_argument("--filter-type", type = str, default = "BPF", help = "Select the type of filter, LPF: Low Pass, HPF: High Pass, BPF: Band Pass")
    parser.add_argument("--cut-off-freq-1", type = float, default = 0.2, help = "First cut-off frequency")
    parser.add_argument("--cut-off-freq-2", type = float, default = 0.3, help = "Second cut-off frequency, for the BPF")
    parser.add_argument("--Cpp", action = "store_true", help = "If Cpp is selected, the filter is implemented in C++ for microcontroller implementation, otherwise in HDL")
    parser.add_argument("--HDL-language", type = str, default = "VHDL", help = "Select the HDL language to implement the filter, select among VHDL, Verilog, SystemVerilog or None")
    return parser.parse_args()
