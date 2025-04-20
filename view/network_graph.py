import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time

def plot_network_graph(frame_plot, data):
    total_rows = len(data)
    steps = 200
    rows_per_step = total_rows // steps

    # Create Matplotlib figure and axes
    fig, ax = plt.subplots(figsize=(8, 5))
    canvas = FigureCanvasTkAgg(fig, master=frame_plot)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill="both", expand=True, padx=10, pady=10)

    # Lists to store data for plotting
    time_axis = []
    total_per_step = []
    netbios_ddos_per_step = []
    syn_ddos_per_step = []
    benign_per_step = []

    state = {"index": 0, "start_time": time.time()}

    def update_plot():
        i = state["index"]
        if i >= total_rows:
            return

        # Read a new chunk of data
        chunk = data.iloc[:i + rows_per_step]
        count_total = len(chunk)

        # Will sum all label from data read
        count_netbios_ddos = (chunk['Label'] == 'NetBIOS').sum()
        count_syn_ddos = (chunk['Label'] == 'Syn').sum()
        count_benign = (chunk['Label'] == 'BENIGN').sum()

        elapsed_time = time.time() - state["start_time"]
        time_axis.append(round(elapsed_time, 2))
        total_per_step.append(count_total)
        
        netbios_ddos_per_step.append(count_netbios_ddos)
        syn_ddos_per_step.append(count_syn_ddos)
        benign_per_step.append(count_benign)

        # Clear and redraw plot
        ax.clear()
        ax.plot(time_axis, total_per_step, label='Total', color='black')
        ax.plot(time_axis, netbios_ddos_per_step, label='DDoS_NETBIOS', color='red')
        ax.plot(time_axis, syn_ddos_per_step, label='DDoS_SYN', color='orange')

        ax.plot(time_axis, benign_per_step, label='BENIGN', color='green')

        info_text = (
            f"Total: {count_total:,}\n"
            f"DDoS_NetBIOS: {count_netbios_ddos:,}\n"
            f"DDoS_SYN: {count_syn_ddos:,}\n"
            f"BENIGN: {count_benign:,}"
        )
        ax.text(0.02, 0.95, info_text, transform=ax.transAxes, fontsize=12,
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

        ax.set_title("All Connections Over Time")
        ax.set_xlabel("Time")
        ax.set_ylabel("Connections")
        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.3)
        canvas.draw()

        # Schedule next update
        state["index"] += rows_per_step
        frame_plot.after(10, update_plot)

    update_plot()
